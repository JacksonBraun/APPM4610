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
    h = .5
    ya = 2 
    [t,y] = EulerExplicit(f,a,b,h,ya)
    
    #Error this and the log I think.

    plt.plot(t,y)
    plt.plot(t,ytrue(t))
    plt.xlabel("time")
    plt.ylabel("y value")
    plt.legend(["Explicit Euler","truth"])
    plt.show()

    plt.plot(t,abs(y - ytrue(t)))
    plt.xlabel("time")
    plt.ylabel("y value (NonLog)")
    plt.yscale("log")
    plt.show()


    print(f"Maximum error between the Explicit Euler and the actual with h={h}, is {abs(y[-1]-ytrue(t[-1]))}")
    return


if __name__ == "__main__":
    main()