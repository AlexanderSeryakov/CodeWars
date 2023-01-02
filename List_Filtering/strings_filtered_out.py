def filter_list(l):
    return [x for x in l if type(x) is int]


assert filter_list([1, 2, 'a', 'b']) == [1, 2], 'Incorrect filtered out'
assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15], 'Incorrect filtered out'
assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123], 'Incorrect filtered out'
