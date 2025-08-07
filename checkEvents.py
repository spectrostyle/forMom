from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


def make_soup(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")

    service = Service()  # no log_path
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup, driver

def page_check(url):
    event_links = []

    soup, _ = make_soup(url)
    events = soup.find_all("li", class_="cpp-MuiListItem-container")

    for event in events:
        a_tag = event.find("a", href=True)
        if a_tag:
            href = a_tag['href']
            event_link = href if href.startswith("http") else url + href
            event_links.append(event_link)

    return event_links

def get_minutes(url):
    links_with_minutes = []

    _, driver = make_soup(url)
    items = driver.find_elements(By.CLASS_NAME, "cpp-MuiListItem-container")

    for item in items:
        try:
            label = item.text.lower()
            if "minutes" in label:
                item.click()
                time.sleep(2)
                current_url = driver.current_url

                links_with_minutes.append(current_url)

                driver.back()
                time.sleep(1)
        except Exception as e:
            print(f"Error on: {e}")

    driver.quit()
    return links_with_minutes
