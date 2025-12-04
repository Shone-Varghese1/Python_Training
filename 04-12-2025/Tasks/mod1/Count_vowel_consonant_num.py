#



#  1. Write a program that reads a string and prints the number of vowels, consonants, and digits.
import re
def count_vowel_consonant_num(text):
    vowel_count=0
    consonant_count=0
    num_count=0
    for char in text:
        if char in 'aeiou':
            vowel_count+=1
        elif re.match(r'[^aeiou 0-9]',char):
            consonant_count+=1
        elif char.isdigit():
            num_count+=1
    print("vowel count: ", vowel_count)
    print("consonant count: ", consonant_count)
    print("num count: ", num_count)
str1=input("enter string : ")
count_vowel_consonant_num(str1)


