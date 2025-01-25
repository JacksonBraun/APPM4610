import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm



def main():
    #do some bull
    k = 2.37
    l = 10
    theta = np.pi/l
    rho = 2.7
    c = .897
    

    u = lambda t,x: np.exp((-k*theta**2*t)/(rho*c))*np.sin(theta*x)

    x=np.linspace(0,l,101)
    t = np. linspace(0,20,101)
    

    plt.style.use('_mpl-gallery')

    # Make data
    
    t, x = np.meshgrid(t, x)

    z = u(t,x)
    # Plot the surface
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(t, x, z, vmin=z.min() * 2, cmap=cm.Reds)
    ax.set(xlabel = ["Time [sec]"],
           ylabel = ["X Distance [cm]"],
           zlabel = ["Temp [K]"])
    

    plt.show()

    return


if __name__ == '__main__':
    main()