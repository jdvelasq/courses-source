import numpy as np

def ackley(x):
    n_dim = len(x)
    p1 = 20 + np.exp(1) - 20 * np.exp(-0.2 * np.mean(x ** 2))
    p2 = np.exp(np.mean(np.cos(2 * np.pi * x)))
    return p1 - p2


def rastrigin(x):
    n_dim = len(x)
    p1 = np.sum(x ** 2)
    p2 = 10 * np.sum(np.cos(2 * np.pi * x))
    return 10 * n_dim + p1 - p2


def rosenbrock(x):
    n_dim = len(x)
    return np.sum(
        [100 * (x[i] ** 2 - x[i+1]) ** 2 + (1 - x[i]) ** 2 for i in range(n_dim - 1)]
    )


def schwefel(x):
    n_dim = len(x)
    return 418.9829 * n_dim + np.sum(x * np.sin(np.sqrt(np.abs(x))))


def sphere(x):
    return np.sum(x ** 2)


def step(x):
    return np.sum(np.floor(x + 0.5) ** 2)
