'''
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
'''

# for row in range(8):
#     for col in range(10):
#         print(col, end=' ')
#     print()

'''
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2

'''
# for i in range(10):
#     for j in range(10):
#         print(i, end=' ')
#     print()

'''
0
0 1
0 1 2
0 1 2 3 


'''
for i in range(10):
    for j in range(i+1):
        print(j, end=' ')
    print()
