import correlation_convolution as cc
import cmath
import math
import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 16
    arguments = [(2 * cmath.pi * i / n) for i in range(n)]
    first_signal = [cmath.sin(3 * x) for x in arguments]
    second_signal = [cmath.cos(x) for x in arguments]

    basic_correlation = cc.correlation(first_signal, second_signal)

    basic_convolution = cc.convolution(first_signal, second_signal)

    fourier_correlation = cc.correlation_fourier(first_signal, second_signal)
    fourier_correlation = list(map(lambda x: x.real, fourier_correlation))
    cc.fourier_corr += cc.fft_count
    cc.fft_count = 0

    fourier_convolution = cc.convolution_fourier(first_signal, second_signal)
    fourier_convolution = list(map(lambda x: x.real, fourier_convolution))
    cc.fourier_conv += cc.fft_count

    print("Number of iteration in basic correlation: {}".format(cc.basic_corr))
    print("Number of iteration in basic convolution: {}".format(cc.basic_conv))
    print("Number of iteration in fourier correlation: {}".format(cc.fourier_corr))
    print("Number of iteration in fourier convolution: {}".format(cc.fourier_conv))

    _, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
    x = np.linspace(0, 2 * cmath.pi, 100)
    y = [math.sin(3 * i) for i in x]
    ax1.plot(x, y)
    ax1.set(title='First signal')
    ax1.grid()

    z = [math.cos(i) for i in x]
    ax2.plot(x, z)
    ax2.set(title='Second signal')
    ax2.grid()

    ax3.plot(arguments, basic_correlation)
    ax3.set(title='Basic correlation')
    ax3.grid()

    ax4.plot(arguments, fourier_correlation)
    ax4.set(title='Fourier correlation')
    ax4.grid()

    ax5.plot(arguments, basic_convolution)
    ax5.set(title='Basic convolution')
    ax5.grid()

    ax6.plot(arguments, fourier_convolution)
    ax6.set(title='Fourier convolution')
    ax6.grid()
    plt.show()


if __name__ == '__main__':
    main()