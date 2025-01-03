def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"there are {num_words} words in the document")
    char_count = get_char_count(text)
    compile_book_report(book_path, num_words, char_count)

# opens the file in path and returns the contents
def get_book_text(path):
    with open(path) as f:
        return f.read()

# splits the file contents into words and counts them
def get_num_words(text):
    # old method that uses count, can instead return words directly with len()
   #count = 0
   #words = text.split()
   #for w in words:
   #    count += 1
   #return count
    # text.split() splits text into a list of words
    words = text.split()
    return len(words)

# counts each character instance and saves it to a dictionary
def get_char_count(text):
    # creates an empty dictonary
    char_count = {}
    # converts the entire text to lower case
    lowered_text = text.lower()
    # iterates through the text, if the character is not in char count,
    # add it to the dictionary and set its instance to 1
    # otherwise, increase the instance count
    for char in lowered_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

# takes all the data and prints it into a nice little book report
def compile_book_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} number of words found in the document")
    sorted_chars = sort_chars(chars)
    for char in sorted_chars:
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    print("--- End report ---")

def sort_chars(chars):
    sorted_chars = []
    for c in chars:
        if c.isalpha():
            sorted_chars.append({"char": c, "num": chars[c]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
    
def sort_on(dict):
    return dict["num"]

main()