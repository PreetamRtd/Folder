import matplotlib.pyplot as plt
import random

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



