words = ['hello', 'chocolate', 'honey', 'cat', 'eggs', 'ELEPHANT']

def print_upper_words(words):
    for word in words:
        print(word.upper())
        

def print_e_words(words):
    for word in words:
        if word[0] == 'e' or word[0]== 'E':
            print(word.upper())

def print_certain_words(words, start_char='c'):
    for word in words:
        for char in start_char:
            if word[0] == start_char:            
                print(word.upper())
