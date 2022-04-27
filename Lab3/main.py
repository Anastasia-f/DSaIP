import walsh
import math
import matplotlib.pyplot as plt


def main():
    n = 16
    arguments = [i * 2 * math.pi / n for i in range(n)]
    function = [math.sin(3 * x) + math.cos(x) for x in arguments]
    walsh_function = walsh.fwt(function)
    walsh_function = [i / n for i in walsh_function]
    inverse_function = walsh.iwt(walsh_function)
    inverse_function = [i * n for i in inverse_function]
    fig, (ax1, ax2, ax3) = plt.subplots(3)

    ax1.plot(arguments, function)
    ax1.set(title='Function plot')
    ax1.grid()

    ax2.plot(arguments, walsh_function)
    ax2.set(title='Fast Walsh Algorithm')
    ax2.grid()

    ax3.plot(arguments, inverse_function)
    ax3.set(title='Inverse function')
    ax3.grid()

    plt.show()


if __name__ == '__main__':
    main()
