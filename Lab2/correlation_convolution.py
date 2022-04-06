import cmath
basic_conv = 0
basic_corr = 0
fourier_conv = 0
fourier_corr = 0
fft_count = 0


def correlation(first, second):
    global basic_corr
    n = len(first)
    z = list()
    for m in range(n):
        s = complex(0)
        for h in range(n):
            s += first[h] * second[(m + h) % n]
            basic_corr += 1
        s /= n
        z.append(s.real)
    return z


def convolution(first, second):
    global basic_conv
    n = len(first)
    z = list()
    for m in range(n):
        s = complex(0)
        for h in range(n):
            s += first[h] * second[m - h]
            basic_conv += 1
        s /= n
        z.append(s.real)
    return z


def correlation_fourier(first, second):
    global fourier_corr, fft_count
    first_image = fft(first, 1)
    second_image = fft(second, 1)
    first_image = list(map(lambda x: x / len(first_image), first_image))
    second_image = list(map(lambda x: x / len(second_image), second_image))
    for i in range(len(first_image)):
        first_image[i] = first_image[i].conjugate() * second_image[i]
        fourier_corr += 1
    return fft(first_image, -1)


def convolution_fourier(first, second):
    global fourier_conv, fft_count
    first_image = fft(first, 1)
    second_image = fft(second, 1)
    first_image = list(map(lambda x: x / len(first_image), first_image))
    second_image = list(map(lambda x: x / len(second_image), second_image))
    for i in range(len(first_image)):
        first_image[i] *= second_image[i]
        fourier_conv += 1
    return fft(first_image, -1)


def fft(input_data, direction):
    global fft_count
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
        w *= w_n
        fft_count += 2
    first_image = fft(first, direction)
    second_image = fft(second, direction)
    result = list()
    for i in range(n):
        result.append(complex(0))
    for i in range(n // 2):
        result[2 * i] = first_image[i]
        result[2 * i + 1] = second_image[i]
    return result
