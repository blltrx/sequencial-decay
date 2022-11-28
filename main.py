import random as r
import matplotlib.pyplot as plt
import numpy as np

def decay():
    x = []
    l1 = []
    l2 = []
    l3 = []

    t1 = 1000000
    t2 = 0
    decayed = 0

    for j in range(50):
        l1.append(t1)
        l2.append(t2)
        l3.append(decayed)
        x.append(j)

        even = 0
        sixs = 0

        for i in t1,t2:
            if i < 0: i = 0
            
        for i in range(t1):
            if r.randint(1,7) % 2 == 0: even += 1

        for i in range(t2):
            if r.randint(1,7) == 6: sixs += 1

        t1 -= even
        t2 -= sixs
        t2 += even
        decayed += sixs


    plt.plot(x, l1, label = "t1")
    plt.plot(x, l2, label = "t2")
    plt.plot(x, l3, label = "decayed")
    plt.title('Sequencial decay')
    plt.legend()
    plt.show()

decay()
