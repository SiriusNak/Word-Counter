from collections import Counter
import re
def get_frequency(text: str)-> list[tuple[str, int]]:
    lowered_text : str = text.lower()
    words : list[str] = re.findall(r'\b\w+\b', lowered_text)
    words_count : Counter = Counter(words)
    return words_count.most_common()

def main()-> None:
    text: str = input('PLease enter your text: ').strip()
    words_frequency : list[tuple[str, int]] = get_frequency(text)
    for words, count in words_frequency:
        print(f'{words} : {count}')

if __name__ == '__main__':
    main()

