# x = range(5)
# print(type(x))
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[-1])
# print(x[4])
# print(x[-5])

# numbers = list(range(5))
# print(numbers)
# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-3])
# print(numbers[-4])
# print(numbers[-5])

# for i in range(5):
#     print(i, end=' ')

# for i in range(5):
#     print("i want to learn web development...")
#     print("something")
# print()


# for i in range(10):
#     print(i+1)

# for i in range(1,11):
#     print(i)

# for i in range(5):
#     print((i+1)*2)

# for i in range(2,11,2):
#     print(i)
# for i in range(1,11,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)
# import math

# for n in 'nikan':
#     print(n)

# for n in [2,4,5,9,0,-1]:
#     print(n*3)

# for n in (3,5,7,8,0):
#     print(n**2)

# for number in {4,9,16,32}:
#     print(math.sqrt(number))
from array import array
import sys
import time

t1 = time.time()
print("time before running first experiment:", t1)
total = 0
for i in range(5_000):

    # number = float(input('enter a number:> '))
    total = total + i

print("total is:", total)
print("size of total as int: ", sys.getsizeof(total))
t2 = time.time()
print("time after running first experiment:", t2)
print("time diff", t2-t1)


t1 = time.time()
print("time before running second experiment:", t1)

numbers = array('i')
for i in range(5_000):
    # number = float(input('enter a number:> '))
    numbers.append(i)

print("total is:", sum(numbers))
# print("total is:", sum([1.2,2.3]))


print("size of numbers as list: ", sys.getsizeof(numbers))
t2 = time.time()
print("time after running second experiment:", t2)
print("time diff", t2-t1)


x = array('i')
# print(x[0])
# x.append(4)
