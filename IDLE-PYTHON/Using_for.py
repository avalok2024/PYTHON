def count_chars_words_lines(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            char_count = len(content)
            word_count = len(content.split())
            line_count = content.count('\n') + 1
            # Adding 1 to count the last line if it doesn't end with '\n'
            print(f"Total characters: {char_count}")
            print(f"Total words: {word_count}")
            print(f"Total lines: {line_count}")
    except FileNotFoundError as e:
        print(f"File '{filename}' not found.")
