# 17. Write a function that finds the longest word in a given sentence.

def find_longest_word(sentence):

    words = sentence.split()
    longest_word = max(words, key=len)

    return longest_word

sentence = "Hello my name is Shone Varghese "
print("Longest word:", find_longest_word(sentence))
