import pdb
import numpy as np
import matplotlib.pyplot as plt
from Integrators import HW5Q1Multistep

def f(t,y):
    return 1-y

def main():
    #part b
    a = 0
    b = 1 
    h = .1
    w0 = 0
    w1 = 1-np.exp(-.1)
    [t,w] = HW5Q1Multistep(f,a,b,w0,w1,h)
    plt.plot(t,w)
    plt.xlabel("time")
    plt.ylabel("y")
    plt.show()

    hc = .01
    wc1 = 1 - np.exp(-.01)
    [tc,wc] = HW5Q1Multistep(f,a,b,w0,wc1,hc)
    plt.plot(t,w)
    plt.plot(tc,wc)
    plt.xlabel("time")
    plt.ylabel("y")
    plt.legend(["h=.1","h=.01"])
    plt.show()










    return





if __name__ == "__main__":
    main()