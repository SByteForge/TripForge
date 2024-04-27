# download.py

import os
import requests
import logging

def download_files(file_urls, download_dir):
    """Download files from the given URLs."""
    os.makedirs(download_dir, exist_ok=True)
    for url in file_urls:
        filename = os.path.basename(url)
        filepath = os.path.join(download_dir, filename)
        logging.info(f"Downloading {filename}...")
        try:
            with open(filepath, "wb") as file:
                file.write(requests.get(url).content)
            logging.info(f"{filename} downloaded successfully.")
        except Exception as e:
            logging.error(f"Failed to download {filename}: {e}")
