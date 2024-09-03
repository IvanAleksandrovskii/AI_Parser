import time
from icecream import ic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from config import settings


def scrape_website(website):
    ic("Launching Chrome browser...")

    chrome_driver_path = settings.chrome.path
    ic(f"ChromeDriver path: {chrome_driver_path}")

    options = Options()
    options.add_argument("--headless")  # Run in headless mode

    driver = None

    try:
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        ic("Chrome browser launched successfully.")

        driver.get(website)
        ic("Page loaded.")

        html = driver.page_source
        time.sleep(10)

        return html

    except WebDriverException as e:
        ic(f"Error launching Chrome browser: {str(e)}")
        raise

    except Exception as e:
        ic(f"Unexpected error: {str(e)}")
        raise

    finally:
        if 'driver' in locals() and driver is not None:
            driver.quit()
