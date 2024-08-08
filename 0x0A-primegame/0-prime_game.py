#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    p = 2
    while p * p <= max_n:
        if sieve[p]:
            for i in range(p * p, max_n + 1, p):
                sieve[i] = False
        p += 1
    primes = [i for i in range(max_n + 1) if sieve[i]]
    return primes

def isWinner(x, nums):
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for p in primes if p <= n)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

