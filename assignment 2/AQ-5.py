
def print_binary(n):
    if n== 0:
        print(0)
        return

    binary = ""
    while n> 0:
        binary = str(n % 2) + binary
        n //= 2

    print(binary)
num=int(input("Enter a number: "))

print("Binary no.:", end=" ")
print_binary(num)
