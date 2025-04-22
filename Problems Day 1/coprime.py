def coprime(i,j):
    return gcd(i,j)==1
def gcd(i,j):
    while j!=0:
        i,j=j,i%j
    return i
n=int(input("Enter a number: "))
for i in range(5, n):
    for j in range(4, i):
        for k in range(3, j):
            if coprime(i,j) and coprime(j,k) and coprime(i,k):
                    print(i,j,k)

