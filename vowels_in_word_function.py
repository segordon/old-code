def get_vowels_in_word(word):
    vowel_str = "aeio"
    vowels_in_word = ""
    for char in word:
        if char in  vowel_str:
            vowels_in_word += char
    return vowels_in_word
