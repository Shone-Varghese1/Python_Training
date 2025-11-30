def remove_vowel(str1):
    new_str="".join([ch for ch in str1 if ch not in "aeiou"])
    return new_str
str1="shone"
print(remove_vowel(str1))