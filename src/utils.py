# utils.py

import requests
import logging

def fetch_html_content(url):
    """Fetch HTML content from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.content
    except requests.RequestException as e:
        logging.error(f"Failed to fetch webpage content from {url}: {e}")
        return None
