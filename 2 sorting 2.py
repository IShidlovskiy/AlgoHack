test_data = [1, 2, 9, 5, 7, 8]


def sort(data: list) -> list:
    for k in range(len(data) - 1):
        max_val = data[0]  # если список не пустой, иначе сломается
        max_pos = 0
        for i in range(len(data)-k):
            if data[i] > max_val:
                max_val = data[i]
                max_pos = i
        data[max_pos], data[-(1+k)] = data[-(1+k)], data[max_pos]
    return data


print(sort(test_data))
