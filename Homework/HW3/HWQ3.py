import pdb

import numpy as np
import matplotlib.pyplot as plt
from Integrators import *

def f(t,y):
    return (1/t**2) - (y/t) -y**2

def totf(t,y):
    return (-2/(t**3)) + (y/(t**2)) - (1/t) - 2*y

def ytrue(t):
    return -1/t

##Gilmans Code (was to check. not used now)
def Taylor_2nd(a,b,h,ya):

     N = int((b-a)/h)
     
     yapp = np.zeros(N+1)
     t = np.zeros(N+1)
     
     yapp[0] = ya
     t[0] = a

     for jj in range(1, N+1):
        tj = a+(jj-1)*h
        t[jj] = tj+h
        ftmp = f(tj,yapp[jj-1])
        ft_tmp = totf(tj,yapp[jj-1])
        yapp[jj] = yapp[jj-1]+h*(ftmp + h/2*ft_tmp)

     return (t,yapp)

def lininterp(t1,t2,y1,y2,tact):
    slope = (y2-y1)/(t2-t1)
    return y1 + slope*(tact-t1)


def main():

    a = 1
    b = 2
    h = .05
    ya = -1
    N = int((b-a)/h)

    #[t,y] = Taylor2(f,a,b,h,ya,totf)
    [t1,y1] = Taylor2(f,a,b,h,ya,totf)
    [t2,y2] = Taylor_2nd(a,b,h,ya)



    plt.plot(t1,y1)
    #plt.plot(t2,y2)
    plt.plot(t1,ytrue(t1))
    plt.xlabel("time")
    plt.ylabel("y value")
    #plt.legend(["Taylor 2 (mine)","Taylor 2 (Gilmans)","truth"])
    plt.legend(["Taylor 2 (mine)","truth"])
    plt.show()

    plt.plot(t1,abs(y1 - ytrue(t1)))
    plt.xlabel("time")
    plt.ylabel("y value (NonLog)")
    plt.yscale("log")
    plt.show()


    print(f"Maximum error between Taylor 2 and the actual with h={h}, is {abs(y1[-1]-ytrue(t1[-1]))}")


    # QUESTION 3b

    tact1 = 1.052
    tact2 = 1.555
    tact3 = 1.978

    # I know I have iterants of .05, so imma just use that.

    titer11indx = 1
    titer12indx = 2

    for i in range(N): 
        if t1[i] + .001  > 1.55  and t1[i] - .001  < 1.55: 
            titer21idx = i
            titer22idx = i +1
    print(f"t interp node 1 {t1[titer21idx]}")
    for i in range(N): 
        if t1[i] + .001  > 1.95  and t1[i] - .001  < 1.95: 
            titer31idx = i
            titer32idx = i +1

    
    yinterp1 = lininterp(t1[titer11indx],t1[titer12indx],y1[titer11indx],y1[titer12indx],tact1)

    yinterp2 = lininterp(t1[titer21idx],t1[titer22idx],y1[titer21idx],y1[titer22idx],tact2)

    yinterp3 = lininterp(t1[titer31idx],t1[titer32idx],y1[titer31idx],y1[titer32idx],tact3)

    errinterp1 = abs(yinterp1-ytrue(tact1))

    errinterp2 = abs(yinterp2-ytrue(tact2))

    errinterp3 = abs(yinterp3-ytrue(tact3))

    print(f"The value of the interpolated y at t = {tact1} is {yinterp1}. This has an error of {errinterp1}")

    print(f"The value of the interpolated y at t = {tact2} is {yinterp2}. This has an error of {errinterp2}")

    print(f"The value of the interpolated y at t = {tact3} is {yinterp3}. This has an error of {errinterp3}")

    return
    







if __name__ == "__main__":
    main()