from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()

# Visit the Flask app
driver.get("http://127.0.0.1:5000/")

# Wait for page to load
time.sleep(1)

# Check for the expected text
assert "Hello, Docker!" in driver.page_source, "❌ Test Failed: Text not found"
print("✅ Test Passed: Found 'Hello, Docker!'")

# Close browser
driver.quit()
