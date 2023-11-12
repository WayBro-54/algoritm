# https://contest.yandex.ru/contest/53027/problems/A/


def input_():
    len, count_iter = map(int, input().split())
    lst = list(map(int, input().split()))
    lst_range = [tuple(map(int, input().split())) for _ in range(count_iter)]
    return lst, lst_range

def found_not_min(lst: list[int], lst_range: list[tuple[int]]):

    for l, r in lst_range:
        min_ = min(lst[l:r + 1])
        max_ = max(lst[l:r + 1])
        if min_ == max_:
            print('NOT FOUND')
        else:
            print(max_)

def main():
    lst, lst_range = input_()
    found_not_min(lst, lst_range)

# https://contest.yandex.ru/contest/53027/problems/B/

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def simplify_fraction(numerator, denominator):
    greatest_common_divisor = gcd(numerator, denominator)
    return numerator // greatest_common_divisor, denominator // greatest_common_divisor

def add_fractions(a, b, c, d):
    common_denominator = b * d
    numerator_sum = (a * d) +( c * b)
    result_numerator, result_denominator = simplify_fraction(numerator_sum, common_denominator)
    return result_numerator, result_denominator

# Ввод данных
# a, b, c, d = map(int, input().split())

# Сложение дробей и упрощение результата
# result_numerator, result_denominator = add_fractions(a, b, c, d)

# Вывод результата
# print(result_numerator, result_denominator)

# https://contest.yandex.ru/contest/53027/problems/D/

def input_():
    in_ = input()
    out_ = input()
    return in_, out_

def annogramma(in_: str = None, out_: str = None):
    x = {}
    for i in out_:
        if i not in x:
            x[i] = 1
        elif i in x:
            x[i] += 1

    for i in in_:
        if i not in x:
            return 'NO'
        elif i in x:
            x[i] -= 1
            if x[i] == 0:
                x.pop(i)
    if x == {}:
        return 'YES'
    return 'NO'
def main():
    in_, out_ = input_()
    print(annogramma(in_, out_))
# main()
# print(annogramma('rat', 'bat'))