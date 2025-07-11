#Write a function that sorts a list of strings alphabetically. 

#["apple", "banana", "cherry", "kiwi", "grape"]

fruit_list=["apple", "banana", "cherry", "kiwi", "grape"]

def sort_list(x):
    return sorted(x)

target=sort_list(fruit_list)

print("The unsorted list :",fruit_list)
print("The sorted list :",target)