from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import logging
from bs4 import BeautifulSoup
from collections import defaultdict


# Configure logging
logging.basicConfig(filename='scraping.log', 
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def scrape_website(url: str) -> str:
    """
    Get player and country data from website.

    Args:
        url str: Website link.

    Returns:
        str: Return html page in string data type.

    Reference:
        https://stackoverflow.com/questions/64032271/handling-accept-cookies-popup-with-selenium-in-python
        https://selenium-python.readthedocs.io/waits.html
        https://scrapfly.io/blog/how-to-click-on-modal-alerts-like-cookie-pop-up-in-selenium/
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()
    
    last_height = 0

    while True:
        driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(5)

        new_height = driver.execute_script("return document.body.scrollHeight")

        logging.info(f"New Height: {new_height}, Last Height: {last_height}")

        if (new_height == last_height):
            break

        else:
            last_height = new_height

    page_source = driver.page_source

    logging.info("Data has beens scraped from website")

    driver.quit()
    return page_source


def extract_player_name_country(content: str) -> dict:
    """
    Extract the HTML string to get player name and the country.

    Args:
        content str: Html page.

    Returns:
        dict: Return dictionary contain player name as key and player country as value.
    """
    player_country_html = BeautifulSoup(content, 'html.parser')

    player_country_data = [element for element in player_country_html.find_all(['span', 'a'], class_=['player__country', 'player__name'])]
    
    if len(player_country_data) % 2 == 0:
        # Initialize defaultdict to store player-country pairs
        player_dict = defaultdict(list)
        player_name = None
        player_country = None

        for element in player_country_data:
            if 'player__name' in element.get('class', []):
                player_name = element.text.strip()
            elif 'player__country' in element.get('class', []):
                player_country = element.text.strip()

            if player_name and player_country:
                player_dict[player_name] = player_country
                logging.info(f"{player_name} and {player_country} has been appended to dicitonary")

                player_name = None
                player_country = None
    else:
        logging.error("The data length count is not even")
        raise Exception("The data length count is not even")

    
    player_country_dict = dict(player_dict)
    logging.info("Player name and country is stored in a dictionary")

    return player_country_dict


def create_json_file(player_country_dict: dict, file_name: str) -> None:
    """
    Store the dictionary in a json file.

    Args:
        player_country_dict dict: Contain the player name and country data.
        file_name str: Specify the file name to save the dictionary.

    Returns:
        None: Because this function only create file and return nothing.
    """
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(player_country_dict, json_file, indent=4, ensure_ascii=False)
    logging.info(f"{file_name} file has been created.")
        


def main():
    url = "https://www.premierleague.com/players?se=719&cl=-1"
    file_name = 'player_country_data.json'
    player_data_html = scrape_website(url)
    player_name_country_dict = extract_player_name_country(player_data_html)
    create_json_file(player_name_country_dict, file_name)


if __name__ == '__main__':
    main()