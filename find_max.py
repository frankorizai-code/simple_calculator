def find_max(a,b,c):
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    return max

num1=float(input("Give the 1st number: "))
num2=float(input("Give the 2nd number: "))
num3=float(input("Give the 3rd number: "))

max_number=find_max(num1,num2,num3)

print(f"\nThe maximun is {max_number}")
