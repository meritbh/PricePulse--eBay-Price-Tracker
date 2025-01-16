import time
import random
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from twilio.rest import Client

# User-Agent rotation for anti-detection
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

# Twilio SMS notification function for batched alerts
def send_batched_sms(items, to_phone):
    if not items:
        print("No items below the threshold to alert.")
        return

    account_sid = "YOUR SID"
    auth_token = "YOUR TOKEN"
    twilio_phone_number = "YOUR PHONE"

    client = Client(account_sid, auth_token)

    body = "Price Alert:\n"
    messages = []
    for item in items:
        item_text = f"{item['title']} - ${item['price']}\n{item['link']}\n\n"
        if len(body + item_text) > 1600:
            messages.append(body.strip())
            body = "Price Alert:\n"
        body += item_text
    messages.append(body.strip())  # Add the last chunk

    try:
        for message_body in messages:
            message = client.messages.create(
                body=message_body,
                from_=twilio_phone_number,
                to=to_phone
            )
            print(f"SMS sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

# Email notification function for batched alerts
def send_batched_email(items, to_email):
    if not items:
        print("No items below the threshold to alert.")
        return

    sender_email = "YOURS@gmail.com"
    sender_password = "YOURS"

    body = "Price Alert:\n\n"
    for item in items:
        body += f"{item['title']} - ${item['price']}\n{item['link']}\n\n"

    msg = MIMEText(body.strip())
    msg["Subject"] = "eBay Price Alert"
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# eBay scraper with SMS and email notifications
def scrape_ebay_and_alert(keyword, price_threshold, phone_number, email, num_pages=3):
    options = Options()
    user_agent = random.choice(USER_AGENTS)
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    alert_items = []

    try:
        for page in range(1, num_pages + 1):
            url = f"https://www.ebay.com/sch/i.html?_nkw={keyword}&_pgn={page}"
            print(f"Scraping page {page}: {url}")
            driver.get(url)
            time.sleep(random.uniform(2, 4))

            items = driver.find_elements(By.CLASS_NAME, "s-item")
            for item in items:
                try:
                    title = item.find_element(By.CLASS_NAME, "s-item__title").text
                    price_text = item.find_element(By.CLASS_NAME, "s-item__price").text
                    if not price_text:
                        continue  # Skip if price is empty
                    price_range = price_text.replace("$", "").replace(",", "").split(" to ")
                    price = float(price_range[0])  # Take the lower bound of the range
                    link = item.find_element(By.CLASS_NAME, "s-item__link").get_attribute("href")

                    if price <= price_threshold:
                        alert_items.append({"title": title, "price": price, "link": link})
                except Exception as e:
                    print(f"Error extracting item: {e}")

        # Send batched SMS alerts
        send_batched_sms(alert_items, phone_number)

        # Send batched email alerts
        send_batched_email(alert_items, email)

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

# Main script execution
if __name__ == "__main__":
    keyword = input("Enter the product keyword to search on eBay: ")
    price_threshold = float(input("Enter the price threshold for alerts: "))
    phone_number = input("Enter your phone number (with country code, e.g., +1234567890): ")
    email = input("Enter your email address for notifications: ")
    scrape_ebay_and_alert(keyword, price_threshold, phone_number, email)
