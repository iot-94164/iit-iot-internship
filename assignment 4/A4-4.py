def histogram(numbers):
    for n in numbers:
        print(f"{n}: {'*' * n}")

num=list(map(int,input("Enter numbers with space: ").split()))
histogram(num)

