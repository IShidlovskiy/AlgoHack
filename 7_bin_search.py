numbers = [i for i in range(0, 1000)]

look_up = 6


def bin_search(nums: list, val: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return -1


for i in range(0, 1000):
    assert bin_search(numbers, i) == i

