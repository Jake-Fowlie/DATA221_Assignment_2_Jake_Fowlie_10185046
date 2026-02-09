"""
Question 3:
Identifies near-duplicate lines in `sample-file.txt` by normalizing lines
(lowercase, removing whitespace and punctuation),
groups lines with identical normalized forms, prints the number of near-duplicate sets,
and shows the first two sets with line numbers.
"""
import string


def normalize_line(line: str) -> str:
    lowercase_line = line.lower()
    characters_to_remove = set(string.punctuation + string.whitespace)

    normalized_characters = [
        ch for ch in lowercase_line if ch not in
                              characters_to_remove]
    normalized_line = ''.join(normalized_characters)
    return normalized_line

def find_near_duplicate_sets(filename: str) -> dict[str, list[tuple[int, str]]]:
    normalized_to_lines: dict[str, list[tuple[int, str]]] = {}

    with open(filename) as file:
        for line_number, original_line in enumerate(file, start=1):
            normalized_line = normalize_line(original_line)
            if normalized_line == "":
                continue

            if normalized_line not in normalized_to_lines:
                normalized_to_lines[normalized_line] = []

            normalized_to_lines[normalized_line].append((line_number, original_line.rstrip('\n')))

    near_duplicate_sets = {
        key: value for key, value in normalized_to_lines.items()
        if len(value) >= 2
    }
    return near_duplicate_sets

def main():
    filename = "sample-file.txt"
    near_duplicate_sets = find_near_duplicate_sets(filename)

    print(f"Number of near-duplicate sets: "
          f"{len(near_duplicate_sets)}")

    sets_as_list = list(near_duplicate_sets.values())

    for set_index, line_group in enumerate(sets_as_list[:2], start=1):
        print(f"\nSet{set_index}:")
        for line_number, original_line in line_group:
            print(f"Line {line_number}: {original_line}")


if __name__ == "__main__":
    main()
