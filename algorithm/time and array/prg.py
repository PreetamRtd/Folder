import matplotlib.pyplot as plt
import random
import time

def plot(a,b):
    plt.plot(a,b)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title("time")
    plt.show()

def gen():
    arr = []
    for j in range(10):
        arr.append(random.randint(0,10))
    return arr

def fun(algo):
    tg = []
    n = []
    z = int(input("enter how many array"))
    for i in range(z):
        n.append(i)
        arr = gen()
        print("before: ",arr)
        t = time.time()
        arr = algo(arr)
        p = time.time()
        print("after: ",arr)
        k = p - t
        tg.append(k)
    plot(n,tg)
