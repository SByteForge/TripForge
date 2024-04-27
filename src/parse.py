# parse.py

from bs4 import BeautifulSoup
import urllib.parse

def parse_html(html_content, url, file_types):
    """Parse HTML content and extract URLs of downloadable files."""
    soup = BeautifulSoup(html_content, "html.parser")
    file_urls = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            absolute_url = urllib.parse.urljoin(url, href)
            # Check if the URL ends with a file extension specified in the config file
            if absolute_url.split(".")[-1].lower() in file_types:
                file_urls.append(absolute_url)
    return file_urls
