def count_number_of(filename, word_to_count):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"'{filename}' could not be found.")
    else:
        num_of_word = contents.lower().count(word_to_count)
        print(f"There are {num_of_word} instances of the word '{word_to_count}' in {filename}.")


count_number_of('Sherlock Holmes.txt', 'the ')
