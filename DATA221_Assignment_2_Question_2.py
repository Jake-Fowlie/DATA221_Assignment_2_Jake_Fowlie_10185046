
import string
import collections


def normalize_word(raw_word: str) -> str | None:
    cleaned_word = raw_word.lower()
    cleaned_word = cleaned_word.strip(string.punctuation)

    alphabetical_characters = sum(1 for chr in cleaned_word if chr.isalpha())
    if  alphabetical_characters < 2 :
        return None

    return cleaned_word if cleaned_word else None

def get_cleaned_words_from_file(filename):
    with open("sample-file.txt", "r") as file:
        file_text = file.read()

        raw_words = file_text.split()
        cleaned_words: list[str] =[]

        for raw_word in raw_words:
            cleaned_word = normalize_word(raw_word)
            if cleaned_word is not None:
                cleaned_words.append(cleaned_word)

        return cleaned_words

def get_bigrams(words: list[str]) -> list[tuple[str, str]] :
    bigrams: list [tuple[str, str]] = []
    for index in range(len(words) - 1):
        bigrams.append((words[index], words[index + 1]))

    return bigrams

def main():
    cleaned_words = get_cleaned_words_from_file("sample-file.txt")

    bigrams = get_bigrams(cleaned_words)

    bigram_frequencies = collections.Counter(bigrams)

    for (first_word, second_word), count in bigram_frequencies.most_common(5):
        print(f"{first_word} {second_word} -> {count}")

if __name__ == "__main__":
    main()