"""In this kata you will create a function that takes a list of non-negative integers and strings and returns a new
list with the strings filtered out."""


def filter_list(l):
    return [x for x in l if type(x) is int]

# Link: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python


assert filter_list([1, 2, 'a', 'b']) == [1, 2], 'Incorrect filtered out'
assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15], 'Incorrect filtered out'
assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123], 'Incorrect filtered out'
