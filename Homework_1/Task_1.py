def longest_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as t:
        text = t.read().split()
        text_sorted = sorted(text, key=len)
        max_len = len(max(text_sorted, key=len))
        longest_word_list = []
        for word in text_sorted:
            if len(word) == max_len:
                longest_word_list.append(word)
        print(f"We've found {len(longest_word_list)} the longest word(s) in file {file_path}: {longest_word_list}.")


if __name__ == '__main__':
    longest_words('text_1.txt')
