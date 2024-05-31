import sys


def main() -> None:
    path_to_file = "C:/Users/Yeon/Desktop/dev/python bookbot/bookbot/books/frankenstein.txt"
    text = read_text_file(path_to_file)
    report(path_to_file, len(text.split()), letter_count(text))
   
def read_text_file(path_to_file: str) -> str: 
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def letter_count(text: str) -> dict:
    text_to_lower = text.lower()
    occr = {}
    for c in text_to_lower:
        occr[c] = occr.get(c, 0) + 1
    return occr

def sort_on(dict):
    return dict[int]

def report(book:str, words:int, word_count: dict[str,int]) -> None:
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    word_count.sort(reverse=True, key=sort_on)
    for item in word_count:
        print(f"The '{item}' character was found {word_count[item]} times")
    print("--- End report ---")

if __name__ == '__main__':
    sys.exit(main())