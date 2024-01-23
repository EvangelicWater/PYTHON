my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#al valor total le sumamos cada elemento de la lista existente

my_list = [10, 1, 8, 3, 5]
total = 0


for i in range(len(my_list)):
    total += my_list[i]

print("Total:"total)


my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

