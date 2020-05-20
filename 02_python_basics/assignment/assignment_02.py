"""
2. write a program loop to get a list sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

list_1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

list_1.sort(key = lambda list_1: list_1[-1])
print (list_1)

list_2 = (4,2,9,6,5,8)

sorted_list = []

highest = list_2 [0]

for n in list_2:
        if n <= highest:
            sorted_list.insert(len(sorted_list)-2, n)
        else:
            sorted_list.append(n)

print (sorted_list)