
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def plot_surface(fn, x_bounds, n_points=50, elev=45, azim=35, figsize=(8, 8)):
    #
    # Grafica la superficie 3D de la función fn(x)
    # con f(x1, x2) = fn([x1, x2])
    #
    xb = x_bounds[0]
    yb = x_bounds[1]
    #
    X = np.linspace(start=xb[0], stop=xb[1], num=n_points)
    Y = np.linspace(start=yb[0], stop=yb[1], num=n_points)
    X, Y = np.meshgrid(X, Y)
    z = np.array([fn(np.array([x, y])) for x, y in zip(X.ravel(), Y.ravel())])
    Z = z.reshape((n_points, n_points))
    #
    fig = plt.figure(figsize=figsize)
    ax = fig.gca(projection="3d")
    # ax.plot_wireframe(X, Y, Z, color='gray', linewidth=0.4)
    ax.plot_surface(
        X,
        Y,
        Z,
        cmap=cm.binary,
        linewidth=1,
        antialiased=False,
        rstride=2,
        cstride=2,
        alpha=0.8,
    )
    ax.plot_wireframe(X, Y, Z, color='gray', linewidth=0.4, alpha=0.8, rstride=2, cstride=2,)
    ax.view_init(elev, azim)
    # ax.set_axis_off()
    plt.show()
    

    
def plot_contour(fn, x_bounds, n_points=50, figsize=(8, 8), levels=20, minimum=None):
    #
    # Grafica la superficie 3D de la función fn(x)
    # con f(x1, x2) = fn([x1, x2])
    #
    xb = x_bounds[0]
    yb = x_bounds[1]
    #
    X = np.linspace(start=xb[0], stop=xb[1], num=n_points)
    Y = np.linspace(start=yb[0], stop=yb[1], num=n_points)
    X, Y = np.meshgrid(X, Y)
    z = np.array([fn(np.array([x, y])) for x, y in zip(X.ravel(), Y.ravel())])
    Z = z.reshape((n_points, n_points))
    #
    fig = plt.figure(figsize=figsize)
    ax = fig.gca()
    ax.contour(X, Y, Z, colors="gray", levels=levels)
    ax.grid()
    if minimum is not None:
        for px, py in minimum:
            plt.plot(px, py, "o", color="red")
    # plt.show()
    
    

def plot_trayectory(stats, fn, x_bounds, minimum):
    
    x = [point[0] for point in stats.x]
    y = [point[1] for point in stats.x]

    plot_contour(
        fn,
        x_bounds=x_bounds,
        minimum=minimum,
    )

    plt.gca().plot(
        x,
        y,
        "o-k",
        alpha=0.5,
    )

    plt.gca().plot(
        x[0],
        y[0],
        "o",
        c="black",
        fillstyle="none",
        markersize=11,
        markeredgewidth=2,
    )

    plt.gca().plot(
        x[-1],
        y[-1],
        "o",
        c="red",
        fillstyle="none",
        markersize=11,
        markeredgewidth=2,
    )

    plt.show()
