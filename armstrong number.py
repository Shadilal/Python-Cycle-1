num = int(input("Enter a number: "))

original = num
count = 0
sum = 0

# Count the number of digits
temp = num
while temp != 0:
    temp = temp // 10
    count = count + 1

# Find the sum of powers of digits
temp = num
while temp != 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

# Check Armstrong number
if sum == original:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
