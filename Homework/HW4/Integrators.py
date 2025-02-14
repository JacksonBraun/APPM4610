import pdb

import numpy as np
import matplotlib.pyplot as plt


def EulerExplicit(f,a,b,h,ya):
    #INPUTS:f=function,a=starttime,b=endtime,h=timestep,ya=initalval
    #OUTPUTS:timevec and yvec
    #JUST DONT BE STUPID
    N = int((b-a)/h)
    yi = np.zeros(N+1)
    ti = np.linspace(a,b,N+1)
    yi[0]=ya
    for i in range(N):
        yi[i+1] = yi[i] + h*f(ti[i],yi[i])
    return [ti,yi]


    


def Taylor2(f,a,b,h,ya,df):
    #INPUTS:f=function,a=starttime,b=endtime,h=timestep,ya=initalval,df=time derivative of f
    #OUTPUTS:timevec and yvec
    #JUST DONT BE STUPID and check df (also larger timesteps maybe needed as I think this is less stable (?????))
    N = int((b-a)/h)
    yi = np.zeros(N+1)
    ti = np.linspace(a,b,N+1)
    yi[0]=ya
    for i in range(N):
        yi[i+1] = yi[i] + h*f(ti[i],yi[i]) + ((h**2)/2) * df(ti[i],yi[i])
    return [ti,yi]

 ## do some random stuff. define functions in your actual place so that these are more usable. If its hard, steal Gillmans

def MidPoint(f,a,b,h,ya):
    N = int((b-a)/h)
    yi = np.zeros(N+1)
    ti = np.linspace(a,b,N+1)
    yi[0]=ya
    for i in range(N):
        yi[i+1] = yi[i] + h/2*(f(ti[i],yi[i])+f(ti[i]+.5*h,yi[i]+.5*h*f(ti[i],yi[i])))
    return [ti,yi]


def RK4(f,a,b,h,ya):

    N = int((b-a)/h)
    yi = np.zeros(N+1)
    ti = np.linspace(a,b,N+1)
    yi[0]=ya
    for i in range(N):
        k1 = f(ti[i],yi[i])
        k2 = f(ti[i] + h/2,yi[i]+h/2*k1)
        k3 = f(ti[i] + h/2,yi[i]+h/2*k2)
        k4 = f(ti[i] + h/2,yi[i]+h/2*k3)
        yi[i+1] = yi[i] + h/6*(k1 + 2*k2 + 2*k3 + k4)

    return [ti,yi]








def main():
    pass

if __name__ == "__main__":
    main()
