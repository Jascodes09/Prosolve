def prime_factors(n, i=2):
    if n == 1:
        return
    if n % i == 0:
        print(i, end=' ')
        prime_factors(n // i, i)  # try same factor again
    else:
        prime_factors(n, i + 1)   # move to next number
n = int(input("Enter a number: "))
print(prime_factors(n))