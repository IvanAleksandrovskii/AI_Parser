import time
from icecream import ic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

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
        time.sleep(2)

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


def extract_body(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for scrypt_or_style in soup(["script", "style"]):
        scrypt_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    ic.enable()
    ic(cleaned_content)
    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)
    ]
