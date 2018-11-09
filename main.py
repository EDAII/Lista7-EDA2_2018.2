import numpy as np
import random
import time
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result



def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)



def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


a = 10
b = 20
c = 30
d = 40



fib_arr = []
fib_memo_arr = []
fib_bottom_up_arr = []

start_time = time.time()
fib(a)
fib_arr.append(time.time() - start_time)

start_time = time.time()
fib(b)
fib_arr.append(time.time() - start_time)

start_time = time.time()
fib(c)
fib_arr.append(time.time() - start_time)

start_time = time.time()
fib(d)
fib_arr.append(time.time() - start_time)



start_time = time.time()
fib_memo(a)
fib_memo_arr.append(time.time() - start_time)

start_time = time.time()
fib_memo(b)
fib_memo_arr.append(time.time() - start_time)

start_time = time.time()
fib_memo(c)
fib_memo_arr.append(time.time() - start_time)

start_time = time.time()
fib_memo(d)
fib_memo_arr.append(time.time() - start_time)


start_time = time.time()
fib_bottom_up(a)
fib_bottom_up_arr.append(time.time() - start_time)

start_time = time.time()
fib_bottom_up(b)
fib_bottom_up_arr.append(time.time() - start_time)

start_time = time.time()
fib_bottom_up(c)
fib_bottom_up_arr.append(time.time() - start_time)

start_time = time.time()
fib_bottom_up(d)
fib_bottom_up_arr.append(time.time() - start_time)




print(fib_arr)
print(fib_memo_arr)
print(fib_bottom_up_arr)

y = [10, 20, 30, 40]
plt.plot(fib_arr, y, color='red')
plt.plot(fib_memo_arr, y, color='blue')
plt.plot(fib_bottom_up_arr, y, color='green')
plt.title("Comparação Tempo de Fibonacci")
red_patch = mpatches.Patch(color='red', label='Naive')
blue_patch = mpatches.Patch(color='blue', label='Memo')
green_patch = mpatches.Patch(color='green', label='Bottom Up')
plt.legend(handles=[red_patch, blue_patch, green_patch])
plt.xlabel('Tempo(s)')
plt.ylabel('Tamanho do vetor')
plt.grid(color='r', linestyle='-', linewidth=0.2)
plt.show()