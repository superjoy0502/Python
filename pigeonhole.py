# import sys

# ascendList = [12,23,34,45,56,67,78,89]
# descendList = [21,32,43,54,65,76,87,98]

# n = int(input())
# for i in range(1, n+1):
#     if n%i == 0:
#         print(i,end = " ")
i = 1
a = 3
n = 8
while i < 20:
    print(str(i) + ": " + str(n))
    if i%2 == 0:
        a = 4
    else:
        a = 3
    n = n + a
    i = i + 1