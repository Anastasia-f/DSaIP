import transform as tr
import cmath as cm
import matplotlib.pyplot as plt
import math


def main():
    # amount of bins equals to sample rate

    n = 16
    arguments = [i * 2 * cm.pi / n for i in range(n)]
    function_values = [math.sin(3 * x) + math.cos(x) for x in arguments]
    function_values_complex = list(map(lambda x: complex(x), function_values)) # применяет lambda функцию к каждому элементу списка

    # DFT
    dft_result = tr.conf_dft(function_values, n, 1)
    reverse_dft_result = tr.conf_dft(dft_result, n, -1)
    reverse_dft_result = list(map(lambda x: x.real, reverse_dft_result))

    # FFT
    fft_result = tr.fft(function_values_complex, 1)
    fft_result = list(map(lambda x: x / n, fft_result))
    reverse_fft_result = tr.fft(fft_result, -1)
    reverse_fft_result = list(map(lambda x: x.real, reverse_fft_result))

    # Amplitude
    dft_amplitude = list(map(lambda x: abs(x), dft_result))
    fft_amplitude = list(map(lambda x: abs(x), fft_result))

    # Phase
    dft_phase = list(map(lambda x: cm.phase(x), dft_result))
    fft_phase = list(map(lambda x: cm.phase(x), fft_result))

    print('Number of DFT operations: {}'.format(tr.dft_counter))
    print('Number of FFT operations: {}'.format(tr.fft_counter))
    print('Efficiency: {}:1'.format(tr.dft_counter // tr.fft_counter))

    # plotting part
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    ax1.plot(arguments, function_values)
    ax1.set(title='Function plot')
    ax1.grid()

    ax2.plot(arguments, dft_amplitude)
    ax2.set(title='Magnitude spectrum plot (DFT)')
    ax2.grid()

    ax3.plot(arguments, dft_phase)
    ax3.set(title='Phase spectrum plot (DFT)')
    ax3.grid()

    ax4.plot(arguments, reverse_dft_result)
    ax4.set(title='Reverse DFT plot')
    ax4.grid()

    fig2, ((ax5, ax6), (ax7, ax8)) = plt.subplots(2, 2)

    ax5.plot(arguments, function_values)
    ax5.set(title='Function plot')
    ax5.grid()

    ax6.plot(arguments, fft_amplitude)
    ax6.set(title='Magnitude spectrum plot (FFT)')
    ax6.grid()

    ax7.plot(arguments, fft_phase)
    ax7.set(title='Phase spectrum plot (FFT)')
    ax7.grid()

    ax8.plot(arguments, reverse_fft_result)
    ax8.set(title='Reverse FFT plot')
    ax8.grid()

    plt.show()


if __name__ == '__main__':
    main()