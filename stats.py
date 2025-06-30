def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(filepath):
    file_contents = get_book_text(filepath)
    num_words = len(file_contents.split())
    print(f"{num_words} words found in the document")
    return num_words

def count_chars(filepath):
    file_contents = get_book_text(filepath)
    letters = {}
    
    for letter in file_contents:
        letter = letter.lower()
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1 
    return letters

def sort_on(items):
    return items["num"]
    
def print_report(filepath):
    unsorted_dict = count_chars(filepath)
    sorted_list = []

    for letter in unsorted_dict:
        if letter.isalpha():
            sorted_list.append({"char": letter, "num": unsorted_dict[letter]})

    sorted_list.sort(reverse=True, key=sort_on)
    word_count = count_words(filepath)
    letter = ""
    count = 0 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_list)):
        letter = sorted_list[i]["char"]
        count = sorted_list[i]["num"]
        print(f"{letter}: {count}")
    print("============= END ===============")

