import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

# Set the screenshot filename
filename = "midjourney_screenshot.png"

# Set the interval in seconds
interval = 600  # 10 minutes

# Initialize the Chrome webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

while True:
    try:
        # Navigate to the webpage
        driver.get("https://www.midjourney.com/app/feed/all/")

        # Take a screenshot using Selenium
        driver.save_screenshot("temp_screenshot.png")

        # Open the screenshot using PIL
        image = Image.open("temp_screenshot.png")

        # Crop the image (optional, adjust coordinates as needed)
        # image = image.crop((100, 100, 800, 600))

        # Save the cropped image
        image.save(filename)

        print(f"Screenshot saved as {filename}")

        # Wait for the specified interval
        time.sleep(interval)

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(60)  # Wait for 1 minute before retrying

    finally:
        # Delete the temporary screenshot file
        try:
            os.remove("temp_screenshot.png")
        except FileNotFoundError:
            pass
