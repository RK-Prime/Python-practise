def calculator(num1, oper, num2):
    if oper == "+":
        print(f"Addition : {num1 + num2}")
    elif oper == "-":
        print(f"Subtraction : {num1 - num2}")
    elif oper == "*":
        print(f"Multiplication : {num1 * num2}")
    elif oper == "/":
        print(f"Remainder : {num1 / num2}")
    else:
        print("Enter a valid option")


def main_calculator():
    a = int(input("Enter the first number : "))
    op = input("Enter the operator +,-,*,/ : ")
    b = int(input("Enter the second number : "))

    calculator(a, op, b)


def lists_a():
    a = [10, 11, 20, 30, 40, 50, 60, 70, 80, 90, 100, 101]

    print(a)

    print(a[0:])  # [10,20,30,40,50,60,70,80,90,100]
    print(a[:])  # [10,20,30,40,50,60,70,80,90,100]
    print(a[0:6])  # [10,20,30,40,50,60]
    print(a[:6])  # [10,20,30,40,50,60]
    print(a[3:7])  # [40,50,60,70]

    even_list = []
    odd_list = []

    for i in a:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(f"Even list : {even_list}")
    print(f"Odd list : {odd_list}")


def lists_b():
    a = [1, 2, 3]
    b = ["a", "b", "c"]
    c = [a] + [b] + ["#", "$", "&"]

    print(c)
    print(c[0])
    print(c[1])
    print(c[2])
    print(c[3])
    print(c[4])
    print(c[0][2])
    print(c[1][2])
    print(c[:][:])


def lists_c():
    a = []
    for i in range(1, 21):
        a.append(i)

    print(a[:])
    print(a[::-1])
    print(a[::1])
    print(a[::2])
    print(a[::-2])


def lists_d():
    a = [0, 1, 2, 3, 4]
    f = a[0]
    s = a[1]
    t = a[2]

    print(f"{f}\n{s}\n{t}")

    # fn,sn,tn = a
    fn, sn, tn, fon, fin = a
    print(f"{fn}\t{sn}\t{tn}\t{fon}\t{fin}")


def lists_e():
    letters = ['a', 'b', 'c', 'd']
    for letter in letters:
        print(letter)
    for index, letter in enumerate(letters):
        print(f"letter : {letter} index : {index}")


def mul(*num):
    nums = []
    nums.append(num)
    print(list(num))


def lists_f():
    letters = ['a', 'b', 'c']
    letters.append('d')
    letters.append('e')
    print(f"{letters}")
    letters.insert(0, '-a')
    print(f"{letters}")
    print(f"{letters.pop()} {letters}")
    print(f"{letters.pop(0)} {letters}")
    letters.remove('a')
    print(f"{letters}")
    del letters[0:1]
    print(f"{letters}")
    letters.clear()
    print(f"{letters}")

    a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(f"{a.count(2)}")
    print(a.index(3))


def tuples_a():
    a = (1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 1)
    b = ('a', 'b', 'c', 'd', 'e')

    print(a, b)

    print(a[0])
    print(a[3])

    print(b[0])
    print(b[3])

    print(a.index(4))
    print(a.count(1))

    print(a.index(1, 3))


def tuples_b():
    a = (5, 2, 3, 4, 1)
    b = ('d', 'b', 'c', 'a')

    print(len(a))
    print(len(b))

    print(max(a))
    print(min(a))

    print(max(b))
    print(min(b))


def dicts_a():
    a = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e'
    }

    print(a)

    del a[3]
    print(a)

    print(a.keys())
    print(a.values())

    a.pop(2)
    print(a)
    print(a.values())
    print(a.keys())

    print(a.items())

    b = a.copy()
    print(b)

    print(b.get(1))

    b.update({
        2: 'c',
        5: 'e'
    })

    print(b)
    print(b.items())
    print(b.keys())
    print(b.values())

    c = sorted(b)
    print(c)


def funcs_a():
    def a(*num):
        print(num)

        nums = []
        for n in num:
            nums.append(n)
        print(nums)

    def b(**var):
        print(var)

    a(1, 2, 3, 4, 5, 6)
    num_a = 10
    b(num1=1, num2=2, num=3, num4=4)


def fizz_buzz_a(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif (input % 3 == 0):
        return "Buzz"
    elif (input % 5 == 0):
        return "Fizz"
    else:
        return input


def sets_a():
    a = {1, 2, 3, 4}
    b = {4, 5, 6, 7}

    a.update(b)
    print(a)

    a.add(9)
    print(a)

    a.discard(9)
    print(a)

    print(a.intersection(b))
    print(a.union(b))

    print(a.issuperset(b))
    print(a.issubset(b))

    print(b.issuperset(a))
    print(b.issubset(a))

    print(a.difference(b))

    print(a.symmetric_difference(b))
    print(sum(a))
    print(sum(b))

    print(a.isdisjoint(b))
    print(b.isdisjoint(a))


def maps():
    a = [1, 2, 3, 4]

    def pow(n):
        return n*n

    b = list(map(pow,a))
    print(b)

    def even(n):
        if n % 2 == 0:
            return True,n
        else :
            return False,n

    c = list(map(even,a))
    print(c)

def filters():
    a = [1,2,3,4]

    def odd(n):
        if n%2 == 0:
            return False
        else :
            return True

    b = list(filter(odd,a))
    print(f"Odd : {b}")

    def even(n):
        if n%2 == 0:
            return True
        else :
            return False

    c = list(filter(even,a))
    print(f"Even : {c}")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def nested_loops():
    n = int(input("Tables upto : "))

    for i in range(1,n+1):
        a = int(input(f"Table of {i} to which number : "))

        if a <= 20:
            for j in range(1,a+1):
                print(f"{i} x {j} = {i*j}")
        else:
            print("Itna jyada tere papa krenge")


def pattern_1():
    n = int(input("Number : "))
    for i in range(n):
        for j in range(i):
            print(i, end=' ')
        print(" ")

def pattern_2():
    n = int(input("Number : "))
    for i in range(n):
        for j in range(i):
            print(j,end=' ')
        print(' ')

def pattern_3():
    n = int(input("Number : "))
    for i in range(n):
        for j in range(i):
            print("* ",end="")
        print(' ')

def pattern_4():
    n = int(input("Number : "))

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j,end=" ")
        print(' ')

def pattern_5():
    n = int(input("Number : "))

    for i in range(1,n+1):
        for j in range(i,n+1):
            print(i, end=' ')
        print('\r')

def pattern_6():
    n = int(input("Number : "))

    for i in range(1, n+1):
        for j in range(i, n+1):
            print(j, end=' ')
        print('\r')

def pattern_7():
    n = int(input("Number : "))

    for i in range(0,n):
        for j in range(i,n):
            print(n,end=' ')
        print(' ')

    for i in range(n, 0, -1):
        for j in range(0,i):
            print(n,end=' ')
        print(' ')

def pattern_8():
    n = int(input("Number : "))
    for i in range(n+1):
        for j in range(0,i+1):
            print(i,end=' ')
        print(' ')

    for i in range(n+1):
        for j in range(0,i+1):
            print(j,end=' ')
        print(' ')

    for i in range(n, 0, -1):
        for j in range(0, i+1):
            print(j, end=" ")
        print(' ')

def pattern_9():
    a = int(input("Number : "))

    for i in range(a):
        for j in range(0,i+1):
            print(f"{i*2+1}", end=' ')
        print(' ')

def pattern_10():
    a = int(input("Number : "))

    for i in range(a-1, -1, -1):
        for j in range(0,i+1):
            print(f"{i*2+1}", end=' ')
        print(' ')

def pattern_11():
    a = int(input("Number : "))
    for i in range(1,a+1):
        for j in range(i,0,-1):
            print(j,end=' ')
        print(' ')

    print('')

    for i in range(a, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print(' ')

def pattern_12():
    start = 1
    stop = 2
    curent_num = stop

    for row in range(stop,6):
        print(f"start : {start} stop : {stop}")
        for col in range(start,stop):
            curent_num-=1
            print(curent_num,end=' ')
        print('')
        start =stop
        stop+=row
        curent_num=stop


def pattern_13():
    n = int(input("Start with : "))
    a = int(input("Number of rows : "))
    for row in range(1, a+1):
        num = n
        for col in range(a, 0, -1):

            if col > row:
                print(' ', end=' ')
            else:
                print(num, end =' ')
                num += 1


        print(' ')

def pattern_14():
    a = int(input('Number : '))


    for i in range(1, a+1):

        for j in range(1, a+1):
            if j <= i:
                print(j, end=' ')
            else:
                print(i, end=' ')

        print(' ')
    print('<------------>')
    for i in range(1, a+1):

        for j in range(1, a+1):
            if j <= i:
                print(i, end=' ')
            else:
                print(j,end=' ')
        print(' ')

if "__main__" != __name__:
    pass
else:
    pattern_14()
