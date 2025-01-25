import numpy as np
import matplotlib.pyplot as plt

import pdb


def main():


    f = lambda x: np.exp(x)

    C1 = lambda x,h: (f(x+h)-2*f(x)+f(x-h))/(h**2)
    C2 = lambda x,h: (-f(x+2*h)+16*f(x+h)-30*f(x)+ 16*f(x-h)-f(x-2*h))/(12*h**2)

    ddf = lambda x: np.exp(x)
    
    x = 7*np.pi/8
    h = 0.1*2**(-np.linspace(0,16,17))

    plt.plot(h,abs(ddf(x)-C1(x,h)))
    plt.title("Err C1")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

    plt.plot(h,abs(ddf(x)-C2(x,h)))
    plt.title("Err C2")
    plt.xscale('log')
    plt.yscale('log')   
    plt.show()




    return




if __name__ == '__main__':
    main()