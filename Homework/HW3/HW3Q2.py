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
    h =  10**(-np.linspace(5,10,5))
    ya = 2
    yh = np.zeros(np.size(h))
    print(f"h val {h}")
    for i in range(6):
        [t,y] = EulerExplicit(f,a,b,h[i],ya)
        yh[i] = y[-1]

        print(f"Counter: {i}")
        print(f"yh Val: {yh[i]}")
    
        
    #Error this and the log I think.

    

    plt.plot(h,abs(yh - ytrue(b*np.ones(6))))
    plt.xlabel("time")
    plt.ylabel("y value (NonLog)")
    plt.yscale("log")
    plt.xscale("log")
    plt.show()


    return


if __name__ == "__main__":
    main()