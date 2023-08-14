test_data = [9, 5, 8, 1, 2]


def sort(data: list):
    for i in range(len(data) - 1):
        for i in range(len(data)-1):
            if data[i] <= data[i+1]:
                continue
            else:
                flag = True
                data[i], data[i+1] = data[i+1], data[i]
    return data


print(sort(test_data))
