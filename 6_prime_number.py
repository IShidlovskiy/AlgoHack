numbers = [i for i in range(2, 1000)]


def only_prime(nums: list) -> list:
    cut_list = []
    for i in range(len(nums)):
        if nums[i] == 1:
            continue
        if nums[i] != 2 and nums[i] % 2 == 0:
            continue
        if nums[i] != 3 and nums[i] % 3 == 0:
            continue
        prime = True
        for n in range(2, nums[i]):
            if nums[i] % n == 0:
                prime = False
                break
        if prime:
            cut_list.append(nums[i])
    return cut_list


print(only_prime(numbers))
