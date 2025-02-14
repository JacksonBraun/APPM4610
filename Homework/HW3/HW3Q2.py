import pdb

import numpy as np
import matplotlib.pyplot as plt
from Integrators import *

def f(t,y):
    return (1+t)/(1+y)

def ytrue(t):
    return np.sqrt(t**2 + 2*t +6)-1

def main():
    a = 1
    b = 2
    h =  10**(-1*np.linspace(1,8,8))
    ya = 2
    yh = np.zeros(np.size(h))
    t = np.linspace(a,b,100)
    print(f"h val {h}")
    plt.plot(t,ytrue(t))
    legend = []
    for i in range(8):


        [t,y] = EulerExplicit(f,a,b,h[i],ya)
        yh[i] = y[-1]

        print(f"Counter: {i}")
        print(f"yh Val: {yh[i]}")
        print(f"Error at final point for h={h[i]} is {abs(yh[i]-ytrue(t[-1]))}")

        plt.plot(t,y)
        legend += str(h[i])
    plt.xlabel("t")
    plt.ylabel("y")
    plt.legend(legend)
    plt.show()
    
        
    #Error this and the log I think.

    

    plt.plot(h,abs(yh - ytrue(b*np.ones(8))))
    plt.xlabel("time")
    plt.ylabel("y value (NonLog)")
    plt.yscale("log")
    plt.xscale("log")
    plt.show()


    return


if __name__ == "__main__":
    main()