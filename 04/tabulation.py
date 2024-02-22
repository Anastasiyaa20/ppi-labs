from matplotlib import pyplot as plt
import math

def func(x: list[float], N: int) -> list[float]:
    """
    Calculate function values for passed array of arguments
    """
    return [math.sin(math.pi* t / N) for t in x]

def tabulate(N: int, a: float, b: float, n: int) -> tuple[list[float], list[float]]:
    x = [a + i * (b - a) / n for i in range(n)]
    y = func(x, N)
    return x, y

def main():
    N = 17
    res = tabulate(N, 0, 50, 1000)

    plt.plot(res[0], res[1])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()