def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")

print("Prime numbers in the given range are:")
for n in range(2, num):
    if is_prime(n):
        print(n)