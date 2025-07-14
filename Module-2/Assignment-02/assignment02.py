#Advanced-Data Structures and Comparison

# Write a Python program that takes two sets from the user and computes their union, intersection, and difference.

# A = {1, 2, 3, 4, 5}

# B = {4, 5, 6, 7, 8}

elements_A = input("Enter the elements of A separated by spaces: ")
elements_B = input("Enter the elements of B separated by spaces: ")

A = set(map(int, elements_A.split()))
B = set(map(int, elements_B.split()))

print("A =",A)
print("B =",B)


union=A.union(B)
print("Union of set A and set B :",union)

intersection=A.intersection(B)
print("Intersection of set A and set B :",intersection)

difference1=A.difference(B)
print("Difference of set A and set B :",difference1)

difference2=B.difference(A)
print("Difference of set B and set A :",difference2)