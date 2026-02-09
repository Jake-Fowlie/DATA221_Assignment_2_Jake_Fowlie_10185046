"""
Question 8:
Scrapes the Data science Wikipedia page, extracts all `<h2>` headings from the main content area,
removes `[edit]`, filters out headings containing “References”, “External links”, “See also”, or “Notes”, a
nd saves the remaining headings to `headings.txt` (one per line).
"""

from typing import Any

import requests
from bs4 import BeautifulSoup

def fetch_page_html(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_h2_heading(html: str) -> list[Any] | list[str]:
    soup = BeautifulSoup(html, "html.parser")

    content_div = soup.find("div", id="mw-content-text")
    if content_div is None:
        return []

    heading_tags = content_div.find_all("h2")

    headings: list[str] = []
    for heading_tag in heading_tags:
        raw_text = heading_tag.text

        cleaned_text = raw_text.replace("[edit]", " ").strip()

        if not cleaned_text:
            continue

        excluded_words = ["References", "External links", "See also", "Notes"]

        if any(word in cleaned_text for word in excluded_words):
            continue

        headings.append(cleaned_text)

    return headings

def save_headings_to_file(headings: list[str], filename: str) -> None:
    with open(filename, "w") as file:
        for heading in headings:
            file.write(heading + "\n")

def main():
    url = "https://en.wikipedia.org/wiki/Data_science"
    output_filename = "headings.txt"

    html = fetch_page_html(url)
    headings = extract_h2_heading(html)

    save_headings_to_file(headings, output_filename)

    for heading in headings:
        print(heading)

if __name__ == "__main__":
    main()