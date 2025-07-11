# Write a function that takes two numbers as input and returns their average. Call the function with different values.

def average(p,q):
    sum=p+q
    return (sum//2)

# call the function for different value
print("Average:",average(7,7))
print("Average:",average(12,6))
print("Average:",average(1,5))


#For user input or taking input from user
p=int(input("Enter the value of p :"))
q=int(input("Enter the value of q :"))
print("Average:",average(p,q))
