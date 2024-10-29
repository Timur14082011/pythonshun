# создаем массив (список) для хранения продуктов
plist = []


# переменная для выбора действий
choose = None

# пока мы не ввели 0, программа будет работать
while choose != "0":
    # таблица выбора действий для измаенения списка
    choose = input(
        "0 - выйди\n1 - добавить в список\n2 - удалить из списка\n3 - показать список\n4 - очистить список\n"
    )
    # команда выхода из программы
    if choose == "0":
        print("Программа завершена")
    # команда добавления элументов в список
    elif choose == "1":
        print("Добавить в список")
        choose1 = input("Введите то что хотите добавит в список: ")
        plist.append(choose1)
    # команда удаления определенного элемента из списка
    elif choose == "2":
        print("Удалить из списка")
        choose1 = input(
            "Введите то что хотите удалить из списка или его порядковый номер: "
        )
        if choose1 in plist:
            plist.remove(choose1)
        # определение число это или нет
        elif choose1.isnumeric():
            num = int(choose1)
            # команда для выбора определенного элемента для удаления
            if num <= len(plist):
                plist.pop(num - 1)
                print("Удаляем элемент с номером", num)
                print("\nСписок продуктов\n")
                for i in range(0, len(plist)):
                    print(f"{i+1}. {plist[i]}")
                print("")
            else:
                print("Номер продукта выходит за границы списка.")
        else:
            print("Такого продукта нет в списке")
    # команда для просмотра элементов находящихся в списке
    elif choose == "3":
        print("\nСписок продуктов\n")
        for i in range(0, len(plist)):
            print(f"{i+1}. {plist[i]}")
        print("")
    # команда для полного очищения списка
    elif choose == "4":
        print("список очищен")
        plist.clear()
    # вывод ошибки при неправильном вводе команды
    else:
        print("Ошибка: введен неверный код")