import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Chain the lists together
chained = itertools.chain(list1, list2, list3)

# Print the elements of the chained iterable
print('chained = itertools.chain(list1, list2, list3)')
print('Chained: ')
print(chained)
chained_list = list(chained)
print('Chained_list: ')
print(chained_list)


for element in chained:
    print(element)


