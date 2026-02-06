import requests
from bs4 import BeautifulSoup

def fetch_page_html(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers= headers)
    response.raise_for_status()
    return response.text

def extract_page_title(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    page_title = title_tag.get_text(strip=True) if title_tag is not None else ""
    return page_title

def extract_first_main_paragraph(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    content_div = soup.find("div", id="mw-content-text")
    if content_div is None:
        return ""

    paragraph_tag = content_div.find_all("p")
    for paragraph in paragraph_tag:
        paragraph_text = paragraph.get_text(strip=True)
        if len(paragraph_text) >= 50:
            return paragraph_text
    return ""

def main():
    url = "https://en.wikipedia.org/wiki/Data_science"

    html = fetch_page_html(url)
    page_title = extract_page_title(html)
    print(f"Page title: {page_title}")

    first_main_paragraph = extract_first_main_paragraph(html)
    print("\nFirst main paragraph:")
    print(first_main_paragraph)

if __name__ == "__main__":
    main()