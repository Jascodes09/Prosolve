'''def is_round_number(num):
    #return str(num).endswith('0')
    return num % 10 == 0
number = int(input("Enter a number: "))
if is_round_number(number):
    print(f"{number} is a round number.")
else:
    print(f"{number} is not a round number.")
'''

def is_round_number(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    return n == 1

number = int(input("Enter a number: "))

if is_round_number(number):
    print(f"{number} is a round number ✅")
else:
    print(f"{number} is not a round number ❌")
