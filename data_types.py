my_list = []
numbers = 10, 20, 30, 40
for number in numbers:
    my_list.append(number)
my_list.insert(1, 15)
list2 = [50, 60, 70]
my_list.extend(list2)
my_list.remove(my_list[-1])
my_list.sort()
print(f"Index for value 30 is: {my_list.index(30)}")
print(my_list)
