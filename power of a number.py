num = int(input("Enter a number: "))
exponent  = int(input("Enter exponent: "))
p=1
for i in range (1,exponent+1):
    p = p*num
print("The Power of","n","^",exponent,"is",p)