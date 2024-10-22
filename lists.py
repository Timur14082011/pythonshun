list = ["молоко" , "сыр", "хлеб", "макароны", "гречка"]

print(list)

index = list.index("молоко")
print("Поиск индекса ",index)

list.append("масло")
print("Новый массив после append ",list)

# list.clear()

# print("Массив после clear ",list)

count = list.count("сыр")
print("Количество в массиве", count)

list.pop(0)
print("После pop удаления", list)

list.insert(3, "слон")
print("После insert", list)
list.sort(reverse=True)
print("Щтсортированный список", list)

list.remove("слон")
print("После remove", list)

list.extend(["колбаса", "огурцы"])
print("Новый объедененный список", list)
