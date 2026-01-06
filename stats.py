def get_num_words(book):
    counter = 0
    list = book.split()
    for word in list:
        counter += 1
    return counter

def letter_count(book):
    letters = book.lower()
    clean = ''.join(char for char in letters if char.isalpha())
    character_count = {}
    
    for letter in clean:
        if letter in character_count:
          character_count[letter] += 1
        else:
            character_count[letter] = 1
    return character_count

def sort_letters(dict):
    new_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return new_dict
