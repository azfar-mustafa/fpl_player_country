# Infinite Scrolling Webpage Scraping

## Overview

This project is to demonstrate on how to scrape data from a webpage that implements infinite scrolling using Python. Infinite scrolling loads additional content dynamically as the user scrolls down the page. This project covers using the Selenium library for browser automation. The example webpage is from this [page](https://www.premierleague.com/players?se=719&cl=-1).

## Prerequisites
* Installed python version of 3.11 and above.
* Google Chrome browser (required for ChromeDriver).

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/azfar-mustafa/infinite-scrolling-scraper.git
   ```

2. **Navigate to the project directory**:

    ```bash
    cd infinite-scrolling-scraper
    ```

3. **Set up a virtual environment** (optional but recommended):

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

4. **Install required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure your `requirements.txt` includes the necessary packages:

    ```txt
    selenium
    beautifulsoup4
    requests
    ```

## Usage

1. **Run the scraping script**:

    ```bash
    python scrape.py
    ```

    This will open a Chrome browser, navigate to the specified URL, accept cookies, and start scrolling down the page to load all content. The data is then scraped and saved to a JSON file.

## Output

The script generates a file named `player_country_data.json` containing a dictionary where the player names are keys and their respective countries are values. Here’s an example of the structure:

```json
{
    "Player Name 1": "Country 1",
    "Player Name 2": "Country 2",
    ...
}
```

## Logging

The script also generates a scraping.log file that logs the scraping process, including heights during scrolling and other debug information.

## Disclaimer

This project is intended solely for learning purposes. The data scraped from the website is used only for educational demonstration and not for any commercial purposes. I do not intend to monetize any data obtained from the website.