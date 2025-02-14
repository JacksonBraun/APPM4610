import numpy as np
import math
import matplotlib.pyplot as plt


def driver():
# Illustration of convergence (looking for the order of the 
# truncation error)


# example 1
#     y = lambda t: (t+1)**2-0.5*np.exp(t)
#     ya = 0.5
#     a = 0
#     b = 2
#     h = 0.2

#example 2
     y = lambda t: t*np.log(t)+2*t
     ya = 2
     a = 1
     b = 2
     
     Nmax = 25
     NN = 2**(-1*np.linspace(1,Nmax,Nmax))

     yapp_end = np.zeros(len(NN))
      
     for jj in range(len(NN)):
     
       h = NN[jj] 
       N = int((b-a)/h)

       [yapp1,t] = explicit_euler(a,b,h,ya)
       yapp_end[jj] = yapp1[N]

     err1 = np.zeros(len(NN))
     
     for j in range(0,len(NN)):
        err1[j] = abs(y(b)-yapp_end[j])
        
     print('err for explicit euler:', err1) 

     plt.plot(NN,err1,label = 'explicit convergence')
     plt.yscale('log')
     plt.xscale('log')
     plt.xlabel('h')
     plt.ylabel('absolute err')
     plt.legend(loc = 'upper left')
     plt.show()


     return 
     
def explicit_euler(a,b,h,ya):

     N = int((b-a)/h)
     
     yapp = np.zeros(N+1)
     t = np.zeros(N+1)
     
     yapp[0] = ya
     t[0] = a

     for jj in range(1, N+1):
        tj = a+(jj-1)*h
        t[jj] = tj+h
        ftmp = eval_f(tj,yapp[jj-1])
        yapp[jj] = yapp[jj-1]+h*ftmp

     return (yapp,t)

     
def  eval_f(t,y):
# example 1
#     f = y -t**2+1

# example 2
     f = 1+y/t

     return f     
     
driver()                    
     
