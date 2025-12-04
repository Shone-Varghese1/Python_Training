# 2. Create a function that takes a sentence and returns a dictionary of word frequencies.

def word_count(text):
    words=text.split()
    freq_dict={}
    for word in words:
        if word in freq_dict:
            freq_dict[word]+=1
        else:
            freq_dict[word]=1
    return freq_dict
str1=input("Enter a sentence")
words_count1=word_count(str1)
print(words_count1)