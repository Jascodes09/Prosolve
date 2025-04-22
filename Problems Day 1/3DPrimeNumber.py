def isprime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def sum_digits(n):
    """Sum the digits of a number."""
    return sum(int(digit) for digit in str(n))
def total_digits(n):
    """Count the number of digits in a number."""
    return len(str(n))
a=int(input("Enter a number: "))
res=[]
n=1
while(len(res)!=a):
    if isprime(n):
        s=sum_digits(n)
        total_digitss=total_digits(n)
        if(isprime(s) and isprime(total_digitss)):
            res.append(n)
    n+=1
print(res)