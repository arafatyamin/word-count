# A function to count the word in a file
def word_counter(word, path):

    count = 0

    with open(path, "r") as file:
        for line in file:
            line = line.strip().lower()
            # Compare the word
            if line == word.lower():
                count += 1

    return count

# A list of words to search
search_words = ["Python", "C", "OOP", "Hello", "Java"]
# input file path
input_file = "./input.txt"
# Loop through in the search_words list
for word in search_words:
    ResultCount = word_counter(word, input_file)
    print(word, "->", ResultCount)
