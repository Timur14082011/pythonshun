plist = []

choose = None

while choose != "0":
    choose = input("0 - выйди\n1 - добавить в список\n2 - удалить из списка\n3 - показать список\n4 - очистить список\n")
    if choose == "0":
        print("Программа завершена")
    elif choose == "1":
        print("Добавить в список")
        choose1 = input("Введите то что хотите добавит в список: ")
        plist.append(choose1)
    elif choose == "2":
        print("Удалить из списка")
        choose1 = input("Введите то что хотите удалить из списка: ")
        if choose1 in plist:
            plist.remove(choose1)
        else:
            print("Такого продукта нет в списке")
    elif choose == "3":
        print("\nСписок продуктов\n")
        for i in range(0, len(plist)):
            print(f"{i+1}. {plist[i]}")
        print("")
    elif choose == "4":
        print("список очищен")
        plist.clear()
    else:
        print("Ошибка: введен неверный код")
