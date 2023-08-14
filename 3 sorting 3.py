test_data = [7, 1, 3, 2, 8]


def sort(data: list):
    if not data:
        return []
    sorted_data = [data.pop()]
    while data:
        item = data.pop()
        for k in range(len(sorted_data)):
            if sorted_data[k] >= item:
                sorted_data.insert(k, item)
                break
    return sorted_data


print(sort(test_data))
