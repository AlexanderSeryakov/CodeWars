"""The goal of this exercise is to convert a string to a new string where each character in the new string is
"(" if that character appears only once in the original string, or ")" if that character appears more than once
in the original string. Ignore capitalization when determining if a character is a duplicate."""


def duplicate_encode(word):
    word = word.lower()
    res_str = ''
    for x in word:
        res_str += '(' if word.count(x) == 1 else ')'
    return res_str

# Link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python
