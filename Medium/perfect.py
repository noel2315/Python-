def is_perfect(num):
    factors = [i for i in range(1, num) if num % i == 0]
    return sum(factors) == num, factors

def print_perfect_numbers_and_factors(n, m):
    num, found = 1, 0
    while found < n:
        perfect, factors = is_perfect(num)
        if perfect: 
            print(f"Perfect number: {num}, First {m} factors: {factors[:m]}")
            found += 1
        num += 1

n, m = int(input()), int(input())
print_perfect_numbers_and_factors(n, m)
