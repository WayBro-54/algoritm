################################
# partition
################################

# Базовым алгоритмом для быстрой сортировки является алгоритм partition, который разбивает набор элементов на две части относительно заданного предиката.
# По сути элементы массива просто меняются местами так, что левее некоторой точки в нем после этой операции лежат элементы, удовлетворяющие заданному предикату, а справа — не удовлетворяющие ему.
# Например, при сортировке можно использовать предикат «меньше опорного», что при оптимальном выборе опорного элемента может разбить массив на две примерно равные части.
#
# Напишите алгоритм partition в качестве первого шага для написания быстрой сортировки.
#
# Формат ввода
# В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 106).
# Во второй строке содержатся N целых чисел ai, разделенных пробелами (-109 ≤ ai ≤ 109).
# В третьей строке содержится опорный элемент x (-109 ≤ x ≤ 109).
# Заметьте, что x не обязательно встречается среди ai.
#
# Формат вывода
# Выведите результат работы вашего алгоритма при использовании предиката «меньше x»: в первой строке выведите число элементов массива, меньших x, а во второй — количество всех остальных.

def input_():
    # ввод данных  ипреобразование к целочисленному типу
    len_lst = int(input())
    lst = list(map(int, input().split()))
    opor = int(input())
    return len_lst, lst, opor


def partition(len_lst, lst, opor):
    ct = 0

    for i in lst:
        if i < opor:
          ct += 1
    return ct, (len_lst - ct)

def main():
    llst, lst, opor = input_()
    le, other = partition(llst, lst, opor)
    print(le)
    print(other)

# main()


# Слияние


def input_():
    # ввод данных  ипреобразование к целочисленному типу
    len_lst_1 = int(input())
    lst_1 = list(map(int, input().split()))
    len_lst_2 = int(input())
    lst_2 = list(map(int, input().split()))
    return len_lst_1, lst_1, len_lst_2, lst_2,

def merge(len1, lst1: list[int], len2, lst2: list[int]):
    res = []
    i, j = 0, 0
    while (i < len1) and (j < len2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    res += lst1[i:]
    res += lst2[j:]
    return res

def main():
    nlst1, lst1, nlst2, lst2 = input_()
    res = merge(nlst1, lst1, nlst2, lst2)
    print(''.join(res))
# main()

##############################################
#           СОРТИРОВКА СЛИЯНИЕМ              #
##############################################

def input_():
    llst = int(input())
    lst = list(map(int, input().split()))
    return lst

def merge(lst1: list[int], lst2: list[int]):
    res = []
    i, j = 0, 0
    while (i < len(lst1)) and (j < len(lst2)):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    res += lst1[i:]
    res += lst2[j:]
    return res

def split_list(lst):
    llst = len(lst) // 2

    l1 = lst[:llst]
    l2 = lst[llst:]

    if len(l1) > 1:
        l1 = split_list(l1)
    if len(l2) > 1:
        l2 = split_list(l2)

    return merge(l1, l2)

def main():
    lst = input_()
    res = split_list(lst)
    print(*res)

# main()

################################################
# Быстрая соритрвока
################################################

# import random
#
# def input_():
#     llst = int(input())
#     lst = list(map(int, input().split()))
#     return lst
#
#
# def quick_sort(lst: list[int]):
#     if len(lst) > 1:
#         x = lst[random.randint(0, len(lst) - 1)]
#         low = [i for i in lst if i < x]
#         mid = [i for i in lst if i == x]
#         hi = [i for i in lst if i > x]
#         lst = quick_sort(low) + mid + quick_sort(hi)
#
#     return lst
#
# def main():
#     lst = input_()
#     res = quick_sort(lst)
#     print(*res)

# main()






