'''
* * * * * * * * * *
'''
from timeit import timeit

# code1 = '''print('* ' * 10)
# '''
# print("first experiment time : ", timeit(code1, number=1000))
# print()
# code2 = '''for row in range(10):
#     print("*", end=" ")
# print()
# '''
# print("second experiment time : ", timeit(code2, number=1000))

'''
* * * * * * * * * *
* * * * * 
* * * * * * * * * * * * * * * * * * * * 
'''
# code1 ="""print("* " * 10)
# print("* " * 5)
# print("* " * 20)
# """
# print("first experiment time : ", timeit(code1, number=10000))
# print()
# code2="""for row in range(10):
#     print("*", end=" ")
# print()
# for row in range(5):
#     print("*" , end=" ")

# print()
# for row in range(20):
#     print("*" , end=" ")
# print()
# """

# print("second experiment time : ", timeit(code2, number=10000))

'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''
# code1 = """for row in range(10):
#     print('* ' * 10)
# print()
# """
# print("first experiment time : ", timeit(code1, number=10000))

# code2 = """for row in range(10):
#     for column in range(10):
#         print("*", end=" ")
#     print()
# print()
# """
# print("second experiment time : ", timeit(code2, number=10000))


# code1 = """for row in range(10):
#     2*3
# """
# print("first experiment time : ", timeit(code1, number=1000000))

# code2 = """for row in range(10):
#     for column in range(10):
#         2*3
# """
# print("second experiment time : ", timeit(code2, number=1000000))

# Exercise 1:
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
# exercise2:
'''
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 

'''

# exercise3:
'''
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
'''
# exercise 4:
'''
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3 
4 4 4 4 4 4 4 4 4 4
.
.
9 9 9 9 9 9 9 9 9 9
'''

# exercise 5:
'''
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9
'''

# exercise 6:
'''
0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7 
      0 1 2 3 4 5 6
        0 1 2 3 4 5 
          0 1 2 3 4
            0 1 2 3
              0 1 2
                0 1 
                  0
            
  
'''
# exercise 7:
'''
1   2   3   4   5   6   7   8   9
2   4   6   8  10  12  14  16  18
.
.
.
.
9  18  27  36  45  54  63  72  81  
'''
'''
>>> type(3)
<class 'int'>
>>> type(3.1)
<class 'float'>
>>> type('hi')
<class 'str'>
>>> type(True)
<class 'bool'>
>>> type([1,2,34])
<class 'list'>
>>> type((1,2,3))
<class 'tuple'>
>>> type({1,2,3,4})
<class 'set'>
>>> x = {1,2,3,4,4,2,3,5}
>>> x
{1, 2, 3, 4, 5}
>>> numbers = [1,2,3,4,4,2]
>>> set(numbers)
{1, 2, 3, 4}
>>> string ='abcdabe1231'
>>> set(string)
{'a', '3', 'b', 'c', 'd', '2', 'e', '1'}
>>> set(string)
{'a', '3', 'b', 'c', 'd', '2', 'e', '1'}
>>> n1 = [1,2]
>>> n2 = [2,1]
>>> if n1 == n2:
... print("ok")
  File "<stdin>", line 2
    print("ok")
        ^
IndentationError: expected an indented block
>>> if n1 == n2:
...  print("ok") 
...
>>> s1 = {1,2}
>>> s2 = {2,1}
>>> if s1 == s2:
...  print("ok")
...
ok
>>> my_list = [100,20,10,50]
>>> for item in my_list:
...  print(item)
...
100
20
10
50
>>> my_list = ["spoon","fork","knife"]
>>> for item in my_list:
...  print(item)
...
spoon
fork
knife
>>> my_list = [  [2,3],  [4,3],  [6,7]   ]
>>> for item in my_list:
...  print(item)
...
[2, 3]
[4, 3]
[6, 7]
>>> for item in my_list:
...  print(item[0],item[1]) 
...
2 3
4 3
6 7
>>> numbers = [1,2,3,4]
>>> sum(numbers)
10
>>> t = 0               
>>> for n in numbers:
...  t += n
... n
  File "<stdin>", line 3
    n
    ^
SyntaxError: invalid syntax
>>> for n in numbers:
...  t += n
...
>>> t
10
>>> exit()


'''