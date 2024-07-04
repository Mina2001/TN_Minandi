def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return len(text.split())

#'example.txt' contains "Hello world"
print(count_words_in_file('question3.txt')) 