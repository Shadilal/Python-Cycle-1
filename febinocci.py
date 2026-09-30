num = int(input("Enter any number: "))

a = 0
b = 1

print("Fibonacci Series for number", num, "is")

for i in range(num):
    print(a)
    c = a + b
    a = b
    b = c
