"""
write a function that returns the largest number from an input list
"""

def find_largest_nb(numbers):
    numbers.sort()
    return numbers [-1]

my_list = [23, 5, 9, 28]
b = find_largest_nb(my_list)
print(b)