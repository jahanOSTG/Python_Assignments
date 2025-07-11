#Write a Python program that creates a new list containing only the duplicate elements from the given list: [1, 5, 6, 5, 1, 2, 3].

num=[1, 5, 6, 5, 1, 2, 3]

#for putting duplicate values
duplicate=[]

for i in num:
    if num.count(i)>1 and i not in duplicate:
        duplicate.append(i)
        
print("The duplicate elements: ",duplicate)