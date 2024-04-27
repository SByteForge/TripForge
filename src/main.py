# main.py

import os
import json
import logging
from src.utils import fetch_html_content
from src.parse import parse_html
from src.download import download_files

def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def main():
    # Setup logging
    setup_logging()

    # Read URL from configuration file
    try:
        with open("config/urls.json", "r") as f:
            config = json.load(f)
            url = config.get("url")
    except Exception as e:
        logging.error(f"Failed to read configuration file: {e}")
        return
    
    
        # Read URL and config file from configuration file
    try:
        with open("config/config.json", "r") as f1:
            config = json.load(f1)
            config_file = config.get("file_types")
    except Exception as e:
        logging.error(f"Failed to read configuration file: {e}")
        return

    # Fetch HTML content from the URL
    html_content = fetch_html_content(url)

    if html_content:
        # Parse HTML content to extract file URLs
        file_urls = parse_html(html_content, url,config_file)

        if file_urls:
            # Directory to save the downloaded files
            download_dir = "data/dump1/"

            # Download files
            download_files(file_urls, download_dir)
        else:
            logging.info("No downloadable files found on the webpage.")
    else:
        logging.error("Failed to fetch webpage content.")

if __name__ == "__main__":
    main()
