"""The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3"""


def rgb(r, g, b):
    if not all(map(lambda x: 0 <= x <= 255, (r, g, b))):
        auxiliary_lst = list(map(lambda j: 0 if j < 0 else 255 if 255 < j else j, (r, g, b)))
        res_lst = [(hex(x).split('x')[1].upper()) for x in auxiliary_lst]
    else:
        res_lst = [(hex(x).split('x')[1].upper()) for x in (r, g, b)]
    for i, elem in enumerate(res_lst):
        if len(elem) < 2:
            res_lst[i] = '0' + elem
    return ''.join(res_lst)

