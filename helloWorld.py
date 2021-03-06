STOP_WORDS = ['a', 'an', 'and', 'are', 'as', 'be', 'by', 
'for', 'if', 'in', 'is', 'it', 'of', 
'or', 'py', 'rst', 'that', 'the', 'to', 'with',]


def get_word_count(curr_list, list_index):
    
    word = curr_list[list_index]
    num_word = curr_list.count(word)

    return word, num_word

# checks that the current word hasn't already been counted
def check_counted_words(curr_word, words_list):
    for word in words_list:
       if curr_word == word: # if the word has already been counted returns true
           return True
    for word in STOP_WORDS: # checks if word is a stop word
        if curr_word == word:
            return True
        
    return False

def get_word_list(file_name):
    words_list = []

    with open(file_name,'r') as file:
        for line in file:
            for word in line.split():
                words_list.append(word)
    return words_list
    


def count_words(file_name):
    words_list = [] # a list that stores each word from a txt file
    counted_words_list =[] # Keeps track of words already counted
    final_word_list = [] # holds the final list of counted words

    words_list = get_word_list(file_name)

    list_index = 0;

    for word in words_list:
        already_counted = check_counted_words(words_list[list_index], counted_words_list)
        if already_counted == False:
            final_word_list.append(get_word_count(words_list, list_index))
            # updates list of already counted words
            counted_words_list.append(words_list[list_index])
            list_index = list_index + 1
        else:
            list_index = list_index + 1

        already_counted = True

   # print(final_word_list)
    return final_word_list

def get_file_list():
    file_list = []
    user_input = ""
    while user_input != "stop":
        user_input = input("Type the name of the file you want to add to the list or type stop to end the list ")
        if user_input != "stop":
            file_list.append(user_input)

    return file_list

def combine_lists(current_list, final_list):
    iterator = 0;
    for item in current_list:
        #print(item)
        for final_item in final_list:
            print(final_item)
            if item[0] == final_item[0]:
                #final_item[1] = final_item[1] + item[1]
                #final_list[iterator][1] = final_item[1] + item[1]
                tempNum = final_item[1] + item[1]
                break
        else:
            final_list.append(item)
        iterator = iterator + 1

    return final_list

def main():
    final_list = []
    file_list = get_file_list()

    for file in file_list:
        print(file)
        final_list = combine_lists(count_words(file), final_list)
        print(final_list)
    # final_list = count_words('text3.txt') # change later
    # print("testign line change")
    # final_list = combine_lists(count_words('text.txt'), final_list)

#if __name__ == '_main_':
main()