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

def main():
    pass

if __name__ == "__main__":
    main()
