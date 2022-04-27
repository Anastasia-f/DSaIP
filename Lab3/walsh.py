def fwt(input_data):
    n = len(input_data)
    if n == 1:
        return input_data
    first = [0 for _ in range(n // 2)]
    second = [0 for _ in range(n // 2)]
    for i in range(n // 2):
        first[i] = input_data[i] + input_data[i + n // 2]
        second[i] = input_data[i] - input_data[i + n // 2]
    first_image = fwt(first)
    second_image = fwt(second)
    result = [0 for _ in range(n)]
    for i in range(n // 2):
        result[i] = first_image[i]
        result[i + n // 2] = second_image[i]
    return result


def iwt(input_data):
    n = len(input_data)
    if n == 1:
        return input_data
    first = [0 for _ in range(n // 2)]
    second = [0 for _ in range(n // 2)]
    for i in range(n // 2):
        first[i] = input_data[i]
        second[i] = input_data[i + n // 2]
    first = iwt(first)
    second = iwt(second)
    result = [0 for _ in range(n)]
    for i in range(n // 2):
        result[i] = (first[i] + second[i]) / 2
        result[i + n // 2] = (first[i] - second[i]) / 2
    return result
