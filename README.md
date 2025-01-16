# PricePulse--eBay-Price-Tracker

## Overview
The **eBay Price Tracker** is a Python-based automation tool designed to scrape product data from eBay, monitor prices, and send notifications via email and SMS when prices drop below a specified threshold. This project is useful for bargain hunters, resellers, and anyone looking to automate eBay price monitoring.

---

## Features

1. **Dynamic Web Scraping**
   - Uses Selenium to scrape product data dynamically, including prices and links.
   - Handles price ranges and skips invalid data.

2. **Notification System**
   - **SMS Alerts**: Sends price drop notifications via Twilio.
   - **Email Notifications**: Delivers detailed alerts to the user’s email using SMTP.

3. **User Input**
   - Allows users to specify:
     - Product keywords to search for.
     - Price thresholds for alerts.
     - Phone numbers for SMS notifications.
     - Email addresses for notifications.

4. **Anti-Detection**
   - Rotates User-Agent strings to reduce the risk of being blocked by eBay.

5. **Batched Notifications**
   - Consolidates multiple alerts into a single email or SMS for efficiency.

---

## Requirements

### Software & Libraries
- Python 3.7+
- Selenium
- Twilio
- WebDriver Manager
- SMTP (for email notifications)
- Random User-Agent rotation

### Accounts
1. **Twilio Account**: Required for SMS alerts.
   - Get your **Account SID**, **Auth Token**, and Twilio phone number.
2. **Email Account**: Gmail is used for email notifications.
   - Enable "Less secure app access" or use an app-specific password for secure authentication.

---

## Usage

1. **Run the Script**:
   ```bash
   python ebay_price_tracker.py
   ```

2. **Input the Following When Prompted**:
   - Product keyword: E.g., "shoes"
   - Price threshold: E.g., "50"
   - Phone number (with country code): E.g., "+1234567890"
   - Email address: E.g., "your-email@gmail.com"

3. **Receive Notifications**:
   - SMS and email alerts will notify you of any price drops.

---

## Example Output

### SMS Alert:
```
Price Alert:
Nike Air Max - $45
https://ebay.com/example-product

Adidas Ultraboost - $40
https://ebay.com/example-product
```

### Email Alert:
```
Subject: eBay Price Alert

Price Alert:
1. Nike Air Max - $45
   Link: https://ebay.com/example-product

2. Adidas Ultraboost - $40
   Link: https://ebay.com/example-product
```

---

## Known Issues & Limitations
1. **Twilio Free Tier**:
   - Limited to sending SMS to verified numbers only.
2. **Email Authentication**:
   - Requires an app-specific password for Gmail accounts.
3. **Dynamic Web Content**:
   - May fail if eBay changes its page structure.

---

## Future Enhancements
- Add support for multiple e-commerce platforms (e.g., Amazon, Walmart).
- Implement a web dashboard for better user interaction.
- Include price trend analysis and visualization.
- Integrate a database (e.g., SQLite) for storing historical data.

---

## Contact
If you find this project impressive and want to discuss potential opportunities, please feel free to reach out:

- **Email**: meritbhusal@gmail.com
- **LinkedIn**: [linkedin.com/in/merit-bhusal](https://www.linkedin.com/in/merit-bhusal-53304832b/)
- **GitHub**: [github.com/meritbh](https://github.com/meritbh)

Thank you for taking the time to review my project. I'm excited about the opportunity to contribute to innovative teams and grow as a software developer!
