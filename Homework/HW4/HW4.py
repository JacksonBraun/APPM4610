import pdb
import numpy as np
import matplotlib.pyplot as plt
from Integrators import EulerExplicit
from Integrators import MidPoint
from Integrators import RK4



def f(t,y): return (y**2)/(1+t)

def y(t): return -1/np.log(t+1)



def main():
    a = 1
    b = 2
    ya = -1/np.log(2)

    hEuler = .025
    hMid = .05
    hRK = .1

    [tEul,yEul] = EulerExplicit(f,a,b,hEuler,ya)

    [tMid,yMid] = MidPoint(f,a,b,hMid,ya)

    [tRK,yRK] = RK4(f,a,b,hRK,ya)

    tdesired = np.linspace(a,b,6)

    #print(f"tvec: {tdesired}")

    ydesEul = np.zeros(len(tdesired))
    count = 0
    for i in range(len(tEul)):
        if tEul[i] in tdesired:
            #print(f"yippie {tEul[i]}")
            ydesEul[count] = yEul[i]
            count +=1
    

    ydesMid = np.zeros(len(tdesired))
    count = 0
    for i in range(len(tMid)):
        if tMid[i] in tdesired:
            #print(f"yippie {tMid[i]}")
            ydesMid[count] = yMid[i]
            count += 1


    ydesRK = np.zeros(len(tdesired))
    count = 0
    for i in range(len(tRK)):
        if tRK[i] in tdesired:
            #print(f"yippie {tRK[i]}")
            ydesRK[count] = yRK[i]
            count +=1
    

    ydes = y(tdesired)
    print(f"Error from Euler Approximation for t = {tdesired} is {ydesEul-ydes} respectfully")
    print(f"Error from Midpoint Approximation for t = {tdesired} is {ydesMid-ydes} respectfully")
    print(f"Error from RK4 Approximation for t = {tdesired} is {ydesRK-ydes} respectfully")

    print(f"function calculations needed for Euler: {len(tEul)}")
    print(f"function calculations needed for Midpoint: {3*len(tMid)}")
    print(f"function calculations needed for RK4: {4*len(tRK)}")


            


    return







if __name__ == "__main__":
    main()

    


