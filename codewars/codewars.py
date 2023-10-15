x = "apple ban"


def add_length(str_):
    if not str_:
        return ValueError('empty string')
    return [i + ' ' + str(len(i)) for i in str_.split(' ')]


# print(add_length(x))

# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
def solution(text, ending):
    return text[-len(ending):] == ending
    # print('hello')


x = 'abbacbdf'
# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

def count(s):
    if not s:
        return {}
    return {i: s.count(i) for i in set(s)}

# print(count(x))

# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

def comp(array1, array2):
    if array1 is None or array2 is None:
        return False

    a_squared = [x * x for x in array1]

    return sorted(a_squared) == sorted(array2)

# еще какое-то легкое задание
# x = [1, 2, 3, 4, 5, 6, ]

# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python


def row_sum_odd_numbers(n):
    first_number = n * (n - 1) + 1
    row_sum = sum(first_number + 2 * i for i in range(n))
    return row_sum
# print(row_sum_odd_numbers(2))

# https://www.codewars.com/kata/52449b062fb80683ec000024/python

def generate_hashtag(s):
    if not s:
        return False
    res = '#'+''.join([i.capitalize() for i in s.split()])
    if len(res) > 140:
        return False
    return res

# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

def expanded_form(num):
    num = str(num)
    count = len(num)
    res = [num[i] + '0' * (count - i - 1) for i in range(count) if num[i] != '0']
    return ' + '.join(res)

# print(expanded_form(70304))




# https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python


def longest_slide_down(pyramid: list[list[int]]) -> int:
    sum = pyramid[0][0]  # присвоим значение первого списка.
    index = 0
    for line in range(1, len(pyramid)):
        now_list = pyramid[line]
        max_value_next_line = max(now_list)
        print(max_value_next_line)
        index = now_list.index(max_value_next_line)
        print(index)
    print(sum)

# longest_slide_down([
#     [75],
#     [95, 64],
#     [17, 47, 82],
#     [18, 35, 87, 10],
#     [20, 4, 82, 47, 65],
#     [19, 1, 23, 75, 3, 34],
#     [88, 2, 77, 73, 7, 63, 67],
#     [99, 65, 4, 28, 6, 16, 70, 92],
#     [41, 41, 26, 56, 83, 40, 80, 70, 33],
#     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#     [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#     [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
# ])






def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n -1)

def ress():
    n, k = map(int, input().split())
    if n < k:
        return 0
    return factorial(n + k -1) // (factorial(k) * factorial(n -1))


# print(ress())


def to24hourtime(hour, minute, period):
    if period == 'pm':
        hour += 12
    if hour == 12 and period == 'am':
        hour = 00
    if len(hour) == 1 and period == 'am':
        hour = '0'+str(hour)
    if minute == 0:
        minute = '00'
    return str(hour) + str(minute)
    # if period == "am":
    #     if hour == 12:
    #         hour = 0
    # else:
    #     if hour != 12:
    #         hour += 12

    # return f"{hour:02d}:{minute:02d}"

# https://www.codewars.com/kata/62c93765cef6f10030dfa92b/train/python


def solution(start, finish):
    count = 0
    while start < finish:
        if finish - start >= 3:
            start += 3
        else:
            start += 1
        count += 1
    return count

# print(solution(828, 849))


# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    url = url.replace('www.', '').replace('http://', '').replace('https://', '')
    return url.split('.')[0]
    # return url.split("//")[-1].split("www.")[-1].split(".")[0]


# print(domain_name("http://www.zombie-bites.com"))

# codewars.com/kata/51edd51599a189fe7f000015/python

def solution(array_a, array_b):
    res = 0
    leng = len(array_a)
    for i in range(leng):
        res += ((array_b[i] - array_a[i]) ** 2) / leng
    return res

# print(solution([10, 20, 10, 2], [10, 25, 5, -2]))


# https://www.codewars.com/kata/54de279df565808f8b00126a/python
# import re
#
# PATTERN = re.compile(r'[0-1]')


# https://www.codewars.com/kata/55983863da40caa2c900004e/python

import itertools
def next_bigger(n):
    t = str(n)
    if t == t[0] * len(t):
        return -1
    per = itertools.permutations(t)
    new_list = set([int(''.join(i)) for i in per])
    
    # x = [ for i in per for j in i if j > n]
    if len(new_list) == 0:
        return -1

# print(next_bigger(2317))

# https://www.codewars.com/kata/60aa29e3639df90049ddf73d/train/python

def binarray(l):
    c, r, d = 0, 0, {0:-1}
    for i in range(len(l)):
        n = l[i]
        if n==0:
            c-=1
        if n==1:
            c+=1
        
        if c in d:
            r = max(r, i-d[c])
        else:
            d[c] = i
        print(c, r, d, i)
    return r
binarray([0,0,1,1,1,0,0,0,0,0])
