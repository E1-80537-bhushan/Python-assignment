#4).Write a function find_longest_word() that takes a list of words and returns the length of the longest
#one.


def find_longest_word(word_list):
    longest_length = 0
    for word in word_list:
        length = len(word)
        if length > longest_length:
            longest_length = length
    return longest_length


word_list = input("Enter a list of words separated by spaces: ").split()


longest_length = find_longest_word(word_list)


print(f"The length of the longest word is: {longest_length}")
