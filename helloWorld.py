# def count_words(file_name):
# def main():
# list.count(x) returns number of times x is in list

def count_words(curr_list, list_index):
    #check_counted_words(word)
    
    word = curr_list[list_index]
    num_word = curr_list.count(word)
    #print(word)
    #print(num_word)
    return word, num_word

# checks that the current word hasn't already been counted
def check_counted_words(curr_word, words_list):
    print("test")

def get_word_list(file_name):
    words_list = []

    with open('text2.txt','r') as file:
        for line in file:
            for word in line.split():
                words_list.append(word)
    return words_list
    


def main():
    # a list that stores each wrod from a txt file
    words_list = []
    counted_words_list =[] # Keeps track of words already counted
    final_word_list = [] # holds the final list of counted words

    words_list = get_word_list('text2.txt')

    list_index = 0;
   # for word in words_list:
   #     count_words(words_list, list_index)
    #    list_index = list_index + 1

    for word in words_list:
        final_word_list.append(count_words(words_list, list_index))
        list_index = list_index + 1

    print(final_word_list)   
    print('Test2')

#if _name_ == _main_:
main()