"""На вход потступаем строка s. Необходимо вернуть длину самого длинного палиндрома в этой строке"""


def longest_palindrome(s):
    """O(n)"""
    if s == s[::-1]:
        return len(s)

    def expand_from_center(s, L, R):
        """L, R - индексы левого и правого символов относительно центрального символа"""
        while 0 <= L and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    start = 0
    end = 0

    for i in range(len(s)):
        """
        length1 находит максимальную длину палиндрома, для центрального символа с чётным индексом 
        'baab' - (ba{центр тут}ab)
        length2 находим максимальную длину палиндрома, для центрального символа с нечётным индексом 
        'lorol' - (lo{r центр тут}ol)
        """
        length1 = expand_from_center(s, i, i)
        length2 = expand_from_center(s, i, i + 1)
        length_max = max(length1, length2)

        """Для того, чтобы не хваринть в памяти все полученные палиндромы и лишь самый длинный на текущий момент, будем 
        проверять, что текущая length_max строго больше текущих значений start и end самого длинного палиндрома,
        если это так, то новый палиндром больше того, чьи значения start и end записаны на данный момент,
        поэтому переопределяем start и end"""
        if length_max > end - start:
            start = i - (length_max - 1) // 2
            end = i + length_max // 2

    return s[start: end + 1]  # end - start + 1 возврат числового значения
