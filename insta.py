from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
import requests

username = "sindhuri03"
url = f"https://www.instagram.com/{username}/"

# Set up Chrome
service = Service()
driver = webdriver.Chrome(service=service)
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Create images folder
os.makedirs("images", exist_ok=True)

# Find all image elements
imgs = driver.find_elements(By.TAG_NAME, "img")

count = 1
for img in imgs:
    src = img.get_attribute("src")
    if src:
        try:
            img_data = requests.get(src).content
            with open(f"images/image_{count}.jpg", "wb") as f:
                f.write(img_data)
            print(f"✅ Saved image_{count}.jpg")
            count += 1
        except:
            pass

driver.quit()
