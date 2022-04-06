import cmath
dft_counter = 0
fft_counter = 0


# DFT
def conf_dft(input_data, length, direction):
    if length:
        n = length
    else:
        n = len(input_data)
    output = list()
    for m in range(n):
        s = complex(0)
        for k in range(n):
            s += input_data[k] * cmath.exp(direction * -2 * complex(0, 1) * cmath.pi * m * k / n)
            if direction == 1:
                global dft_counter
                dft_counter += 1
        if direction == 1:
            s /= n
        output.append(s)
    return output


# FFT
def fft(input_data, direction):
    n = len(input_data)
    if n == 1:
        return input_data
    first = list()
    second = list()
    for i in range(n // 2):
        first.append(complex(0))
        second.append(complex(0))
    w = complex(1, 0)
    w_n = cmath.exp(-2 * complex(0, 1) * cmath.pi * direction / n)
    for i in range(n // 2):
        first[i] = input_data[i] + input_data[i + n // 2]
        second[i] = (input_data[i] - input_data[i + n // 2]) * w
        if direction == 1:
            global fft_counter
            fft_counter += 2
        w *= w_n
    first_image = fft(first, direction)
    second_image = fft(second, direction)
    result = list()
    for i in range(n):
        result.append(complex(0))
    for i in range(n // 2):
        result[2 * i] = first_image[i]
        result[2 * i + 1] = second_image[i]
    return result
