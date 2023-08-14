numbers = [i for i in range(2, 1000)]


def only_prime(nums: list) -> list:
    primes = []
    while nums:
        prime = nums[0]
        primes.append(prime)
        nums = [num for num in nums if num % prime != 0]
    return primes


print(only_prime(numbers))
