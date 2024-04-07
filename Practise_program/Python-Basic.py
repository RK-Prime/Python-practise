# a = 10

# print(f'normal division : {10/3}')
# print(f'Remainder : {10%2}')
# print(f'floor division : {10//3}')

# print(f'Rohan{a}Katyal')

# shorthand method
# prompt and direct print method

# a = print(input('Input first number : '))
# b = print(input('Input second number : '))


# a, b = [], []
# n = int(input('Enter list size : '))

# for i in range(n):
#     a.append(i)
#     b.append(i+1)

# for i in range(0,n):
#     a[i] = i
#     b[i] = i+1

# ^ will give error as list size is initially zero

# print(a, b)

# a = []
#
# for i in range(10):
#     a.append(i+1)
#
# print(a)
# b = []
# c = []
#
# for i in a:
#
#     if i % 2 == 0:
#         b.append(i)
#     elif i % 2 != 0:
#         c.append(i)
#
# print(b, c)
#
#

# a = [1]*20
# b = [a]*2
#
# print(a)
# print(b)


# a = list('RohanKatyal')
#
# print(a)

# a = 'RohanKatyal'
#
# print(a[0:])
# print(a[:])
# print(a[:5])
# print(a[5:])
#
# b = []
#
# for i in range(10):
#     b.append(i+1)
#
# print(b)
# print(f'Even List : {b[1::2]}')
# print(f'Odd List : {b[::2]}')

# for j in b:
#     if j % 2 == 0:
#         print(f'{j} => {b[1::2]}')
#     else:
#         print(f'{j} => {b[::2]}')

# print(list(range(10)))

# short had method of creating a list with a normal format(i.e. 0,1,2,3,4,5,....)
# c = list(range(10))
#
# print(c)
# print(c[:9])
# print(c[3:8])
# print(c[7::-1])
# print(c[8:2:-1])
# print(c[::-1])
# print(c[::])
#
# d = list(range(10))
#
# print(f'd : {d}')
#
# e = list(range(1, 11))
#
# first, second, *others = e
#
# print(first)
# print(second)
# print(others)
#
# for i in enumerate(e):
#     print(f'Tuple : {i}')
#     print(f'index : {i[0]}, number : {i[1]}')

#
# a = ['a', 'b', 'c', 'd']
# print(a)
#
# print(a.pop())
# print(a)
#
# a.append('d')
# print(a)
#
# a.reverse()
#
# print(a)
#
# b = [1] * 10
#
# print(b)
#
#
# for i in range(len(b)):
#     b[i] = 'a'
#     b.append(i*0)
#
# print(b)
# print(b.count(0))
# print(b.count('a'))


# a: list[int] = [1,2,3]
# b: list[str] = ['a','b','c']
#
# c = [a] + [b] + ['!', '@', '#', '$']
#
# print('a : ', a)
# print('b : ', b)
# print('c : ', c)
#
# print('a[0]: ',a[0])
# print('b[0]: ',b[0])
#
# print('c[0]: ',c[0])
# print('c[1]: ',c[1])
# print('c[2]: ',c[2])
#
# print('c[0][0]: ',c[0][0])
# print('c[0][1]: ',c[0][1])
#
# print('c[1][0]: ', c[1][0])
# print('c[1][1]: ', c[1][1])
#
# print('c[5]: ', c[5])
#
# print('c[:][:]: ', c[:][:])


# letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#
# count = 0
#
# for letter in letters:
#     count += 1
#
# print(count)
#
# for index, letter in enumerate(letters):
#     print(f'index : {index+1}, letter : {letter}')


# def mul(*num):
#     nums = []
#     nums.append(num)
#     print(nums)
#
# mul(1,2,3,4,5,6)

# a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1)
#
# print(a)
# print(a[0])
# print(a[:8])
# print(a[::-1])
# print(a[1::2])
# print(a[::1])
# print(a[::-2])
#
# print(a.index(8))
#
# print(a.index(1, 2))
#
# print(len(a))
#
# print(max(a))
# print(min(a))

#
# a = {
#     'a': '1',
#     'b': '2',
#     'c': '3',
#     'g': '7',
#     'h': '8',
#     'd': '4',
#     'e': '5',
#     'f': '6',
#     'i': '9',
#     'j': '10'
# }
#
#
# print(a)
#
# print(a['a'])
#
# print(a.keys())
# print(a.values())
#
# a.pop('j')
# print(a)
#
# a.update({
#     'j': '10',
#     'i': '10-1'
# })
# print(a)
#
# print(a.get('a'))
# b = a.copy()
#
# print(b)
#
# print(b.items())
#
# c = b.items()
#
# for i in c:
#     print(i)
#
# d = sorted(b)
#
# print(d)
#
#
# def args_func(*args):
#     print('args create a tuple')
#     print(args)
#
#
# args_func(1,2,3,4,5,6)
#
#
# def kwargs_func(**kwargs):
#     print('kwargs create a dictionary')
#     print(kwargs)
#
#
# kwargs_func(num1=1, num2=2, num3=3)


# def print_all_args(*args):
#     for arg in args:
#         print(arg)
#     print(args)
#
# a = [1,2,3,4,5,6,7,8,9,10]
#
# # print_all_args(*a)
#
#
# def print_all_kwargs(**kwargs):
#
#     print(kwargs)
#     for key, item in kwargs.items():
#         print(f'key: {key}, item: {item}')
#
#
# # print_all_kwargs(a=1, b=2, c=3, d=4)
#
# dict_a = {
#     '0': 'a',
#     '1': 'b',
#     '2': 'c',
#     '3': 'd',
#     '4': 'e'
# }

# print_all_kwargs(**dict_a)


# def student_info(**kwargs):
#     for field, value in kwargs.items():
#         print(f'Feild : {field} and Value : {value}')
#
# student_info(fname='Rohan',lname='Katyal',course='BTech')
# student_info(fname='Rahul',lname='Gatuam',course='Btech',branch='CSE')
#


# give an integer n, returns sting array answer.
# answer[i] == 'FizzBuzz' if i is divisible by 3 and 5
# answer[i] == 'Fizz' if i is divisible by 3.
# answer[i] == 'Buzz' if i is divisible by 5.
# answer[i] == i as str if none of above is true


# def fizz_buzz_a():
#
#     n = int(input('Enter the value of n: '))
#     answer = []
#
#     for i in range(1, n+1):
#         if (i % 3 == 0) and (i % 5 == 0):
#             answer.append("FizzBuzz")
#         elif (i % 3 == 0):
#             answer.append("Fizz")
#         elif (i % 5 == 0):
#             answer.append("Buzz")
#         else:
#             answer.append(i)
#
#     return answer
    #print(answer)

# for i in range(1,n+1):
#     answer.append(fizz_buzz_a(i))
#
# print(answer)


def set_func():
    a = {1,2,3,4}
    b = {5,6,7,8}

    print(a)
    print(b)

    a.update(b)
    print(a)

    a.add(9)
    print(a)

    a.discard(4)
    print(a)

    c = a.intersection(b)
    print(c)

    d = a.union(b)
    print(d)

    print(a.issuperset(b))
    print(a.issubset(b))
    print(b.issubset(a))

    print(a-b)
    print(a.difference(b))

    print(a.symmetric_difference(b))
    print(sum(a))
    print(sum(b))

    print(a.isdisjoint(b))
    print(b.isdisjoint(a))
    print(b.isdisjoint(b))

    e = {'a','b','c'}

    print(a.isdisjoint(e))
    print(e.isdisjoint(a))


# set_func()

def map_func():

    a = [1,2,3,4,5,6,7,8,9,10]

    def sum(i):
        return i*i

    b = list(map(sum, a))

    print(b)

#map_func()


def map_func_b():
    a = [0,1,2,3,4,5,6,7,8,9,10]

    # map function ek function pe iterate krta hai,
    # aur woh ek list ki harr ek values ko one by one,
    # uss function pe iterate krta hai, aur uski values ko,
    # fir hum built-in list function ka use krke,
    # new list variable main store krate hain,

    def power_func(input_val):
        return input_val**2

    # b = list(map(power_func, a))

    def even(n):
        if n% 2 == 0:
            return 'Even', n

        else:
            return 'Odd', n

    b = list(map(even, a))

    print(b)

#map_func_b()


def filter_func():

    a = [1,2,3,4,5,6,7,8,9,10]

    def odd(n):

        if n%2 == 0:
            return False
        else:
            return True

    b = list(filter(odd,a))
    print(f'Odd: {b}')

    # filter function bhi map ki tarah ek function pe ek list ki values,
    # ko iterate krta hai lekin, map function unn values ko k hi list,
    # main rehnedeta hai, lekin filter ek new list bana ke unhe bahar,
    # krdeta hai, filter unn values ko comparison basis pe out krleta hai

#filter_func()


def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n*factorial_rec(n-1)
def factorial_iter(n, val=1):
    if n > 1:
        for i in range(1, n + 1):
            val *= i
    else:
        val = 1
    return val

# num = 10
# print(factorial_rec(num))
# print(factorial_iter(num))


def nested_loops(a, n, count=10):

    print(f'Tables of {a} to {n}')

    for i in range(a, n+1):
        print(f'Table of {i}')

        for j in range(1, count+1):
            print(f'{i}*{j} = {i*j}')

#nested_loops(3,10)

def nested_loop_b(n):

    j = 0
    for i in range(1,n+1):

        print(f'i:{i}')
        while j<i:
            print(f'j:{j}')
            j+=1

# nested_loop_b(10)



#import random

# for i in range(3):
#
#     # print(random.random())
#
#     print(random.randint(3, 10))
#
# members = ['a','b','c','d','e','f','g']
#
#
# for i in range(len(members)):
#     print(random.choice(members))

#
import random
class Dice:

    def roll(self):
        a = random.randint(1,6)
        b = random.randint(1,6)
        t = (a,b)
        return t

# a_dice = Dice()
#
# print(a_dice.roll())


class Student:

    def __init__(self, name, course, branch):

        self.name = name
        self.course = course
        self.branch = branch

    def info(self):
        print(f'Name : {self.name}')
        print(f'Course : {self.course}')
        print(f'Branch: {self.branch}')


s1 = Student('Rohan', 'BTech', 'CSE')
s2 = Student('Haris', 'BTech', 'CSE')

s1.info()
s2.info()


