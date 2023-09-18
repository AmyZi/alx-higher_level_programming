#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

def fetch_non_interactive_content(url):
    # Send a request to the URL
    response = requests.get(https://intranet.alxswe.com/projects/331)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and extract the non-interactive content (e.g., text)
        non_interactive_content = soup.get_text()

        return non_interactive_content
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    # Replace with the URL of the web page you want to scrape
    target_url = "https://intranet.alxswe.com/projects/331"

    non_interactive_content = fetch_non_interactive_content(target_url)

    if non_interactive_content:
        # Print or process the non-interactive content as needed
        print("Non-interactive content:")
        print(non_interactive_content)
    else:
        print("Failed to retrieve non-interactive content.")
