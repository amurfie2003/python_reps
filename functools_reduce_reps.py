#Challenge: Create a function that takes a list of integers and returns the 
#product of all the elements in the list.
import functools
numbers = [1, 2, 3, 4, 5, 6]

def multiply(list_numbers):
    if not list_numbers:
        return []
    return functools.reduce(lambda x, y: x * y, list_numbers)


#test
assert multiply(numbers) == 720
assert multiply([]) == []

print(f"[1, 2, 3, 4, 5, 6] = {multiply(numbers)}")
print(f"[] = {multiply([])}")