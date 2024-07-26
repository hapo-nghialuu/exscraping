# Homes Spider

This project contains a Scrapy spider named `homes` that crawls real estate data from the website [homes.co.jp](https://www.homes.co.jp/). The spider extracts the content of `<h2>` elements inside specific `<div>` elements with class `lg:mb-6 my-4`.

## Prerequisites

- Python 3.6 or higher
- Scrapy 2.x or higher
- Mac OS or Linux

## Setup

1. **Clone the repository** (if using a version control system):

    ```bash
    git clone <repository-url>
    cd homes_spider
    ```

2. Create a virtual environment

    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Spider

1. Navigate to the project directory and run the spider

    ```bash
    cd homes_spider
    scrapy crawl homes
    ```

2. Navigate to the project directory and run the spider

    ```bash
    cd nifty_spider
    scrapy crawl nifty
    ```
