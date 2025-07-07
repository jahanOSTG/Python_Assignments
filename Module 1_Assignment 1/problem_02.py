#Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.

numb1 = int(input("Enter the first number : "))
numb2 = int(input("Enter the second number : "))
operator=input("Select operator (+, -, *, /): ")

if operator=='+':
    print(numb1+numb2)
elif operator=='-':
    print(numb1-numb2)
elif operator=='*':
    print(numb1*numb2)
elif operator=='/':
    print(int(numb1/numb2))
else:
    print("Invalid")
    