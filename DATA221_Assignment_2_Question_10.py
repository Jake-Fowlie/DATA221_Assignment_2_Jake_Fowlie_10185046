from typing import List, Tuple

def find_lines_containing(filename: str, keyword: str) -> List[Tuple[int, str]]:
    """
        Returns a list of (line_number, line_text) for lines that contain keyword
        (case-insensitive). Line numbers start at 1.
    """
    keyword_lower = keyword.lower()
    matching_lines: List[Tuple[int, str]] = []

    with open(filename, "r") as file:
        for line_number, line_text in enumerate(file,start=1):
            if keyword_lower.lower() in line_text.lower():
                matching_lines.append((line_number, line_text.strip("\n")))

    return matching_lines

def main():
    filename = "sample-file.txt"
    keyword = "lorem"

    matches = find_lines_containing(filename, keyword)

    print(f"Number of matching lines:  {len(matches)}")

    print("\nFirst 3 matching lines:")
    for line_number, line_text in matches[:3]:
        print(f"{line_number}: {line_text}")

if __name__ == "__main__":
    main()