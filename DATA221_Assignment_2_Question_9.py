import requests
from bs4 import BeautifulSoup
import csv


def scrape_machine_learning_table():
    url = "https://en.wikipedia.org/wiki/Machine_learning"
    headers_browser = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers_browser)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    # 1. Locate the main content area
    content_div = soup.find('div', id='mw-content-text')
    if not content_div:
        return

        # 2. Find the first table with at least 3 data rows
    target_table = None
    for table in content_div.find_all('table'):
        # A "data row" typically contains <td> tags
        data_rows = [row for row in table.find_all('tr') if row.find('td')]
        if len(data_rows) >= 3:
            target_table = table
            break

    if not target_table:
        print("No suitable table found")
        return

    # 3. Extract all rows to determine the maximum column count
    all_rows_raw = []
    max_cols = 0
    for tr in target_table.find_all('tr'):
        cells = tr.find_all(['th', 'td'])
        row_content = [cell.get_text(strip=True) for cell in cells]
        if row_content:
            all_rows_raw.append(row_content)
            if len(row_content) > max_cols:
                max_cols = len(row_content)

    # 4. Handle Headers: Use <th> if present, otherwise col1, col2, etc.
    first_tr = target_table.find('tr')
    has_th = first_tr.find('th') is not None

    if has_th:
        headers = all_rows_raw[0]
        data_to_save = all_rows_raw[1:]
    else:
        headers = [f"col{i + 1}" for i in range(max_cols)]
        data_to_save = all_rows_raw

    # 5. Padding: Ensure all rows have the same number of columns
    def pad(row, length):
        return row + [''] * (length - len(row))

    final_headers = pad(headers, max_cols)
    final_data = [pad(row, max_cols) for row in data_to_save]

    # 6. Save to wiki_table.csv
    with open('wiki_table.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(final_headers)
        writer.writerows(final_data)

    print(f"Successfully saved table to wiki_table.csv with {max_cols} columns")


if __name__ == '__main__':
    scrape_machine_learning_table()