def print_upper_words(word_list):
    """This should accept a list [] or words and print out each word in uppercase on a separate line:
    print_upper_words(['bake','herO','BlInK']) should yield:
    BAKE
    HERO
    BLINK
    """
    for word in word_list:
        print(word.upper())

def print_starts_with_e(word_list):
    """This should accept a list [] or words and print out each word in uppercase on a separate line, only if the word starts with the letter e or E:
    print_upper_words(['bake','herO','BlInK', 'Elephant','eager']) should yield:
    ELEPHANT
    EAGER
    """
    for word in word_list:
        if word[0] == 'e' or word[0] =='E':
            print(word.upper())

def print_upper_starts_with_x (word_list, letter_list):
    for word in word_list:
        for letter in letter_list:
            if letter == word[0]:
                print(word.upper())