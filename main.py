import logging
import os
import selenium.webdriver as webdriver
from dotenv import load_dotenv
from selenium.webdriver.common import by
from config import website_url

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# 1. Launch browser
driver = webdriver.Chrome()
logger.info("launched browser")
# 2. Navigate to url 'http://automationexercise.com'
logger.info(f"navigted to {website_url}")
driver.get(website_url)
# 3. Verify that home page is visible successfully

# 4. Click on 'Signup / Login' button
loginbutton = driver.find_element(by.By.LINK_TEXT, "Signup / Login")
loginbutton.click()
# 5. Verify 'New User Signup!' is visible
signup_label = driver.find_element(by.By.CLASS_NAME, "signup-form").find_element(
    by.By.TAG_NAME, "h2"
)
assert signup_label.is_displayed() and signup_label.text == "New User Signup!"


# 6. Enter name and email address
name_field = driver.find_element(by.By.CSS_SELECTOR, "[data-qa='signup-name']")
email_field = driver.find_element(by.By.CSS_SELECTOR, "[data-qa='signup-email']")
email = os.getenv("account_1_email")
name = os.getenv("account_1_name")
name_field.send_keys(name or "")
email_field.send_keys(email or "")

# 7. Click 'Signup' button
signup_button = driver.find_element(by.By.CSS_SELECTOR, "[data-qa='signup-name']")
signup_button.click()
# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
title = driver.title
url = driver.current_url
print(f"{title} loaded successfully, at {url}")
driver.quit()
