# def count_words(file_name):
# def main():
# list.count(x) returns number of times x is in list

STOP_WORDS = ['a', 'an', 'and', 'are', 'as', 'be', 'by', 
'for', 'if', 'in', 'is', 'it', 'of', 
'or', 'py', 'rst', 'that', 'the', 'to', 'with',]


def count_words(curr_list, list_index):
    #check_counted_words(word)
    
    word = curr_list[list_index]
    num_word = curr_list.count(word)

    return word, num_word

# checks that the current word hasn't already been counted
def check_counted_words(curr_word, words_list):
    for word in words_list: # iterates through list
       if curr_word == word:
           #print(curr_word, word)
           return True
        
    return False

def get_word_list(file_name):
    words_list = []

    with open('text2.txt','r') as file:
        for line in file:
            for word in line.split():
                words_list.append(word)
    return words_list
    


def main():
    # a list that stores each word from a txt file
    words_list = []
    counted_words_list =[] # Keeps track of words already counted
    final_word_list = [] # holds the final list of counted words

    words_list = get_word_list('text2.txt')

    list_index = 0;

    for word in words_list:
        already_counted = check_counted_words(words_list[list_index], counted_words_list)
        if already_counted == False:
            final_word_list.append(count_words(words_list, list_index))
            # updates list of already counted words
            counted_words_list.append(words_list[list_index])
            list_index = list_index + 1
        else:
            list_index = list_index + 1

        already_counted = True

    print(final_word_list)   
    print('Test2')

#if _name_ == _main_:
main()