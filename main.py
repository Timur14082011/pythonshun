# slovar = {
#     "помидор":"фрукт",
#     "арбуз":"ягода",
#     "age":100
# }
# print(slovar["арбуз"])

# slovar.pop("age")
# slovar["Новое поле"] = True
# print(slovar)
# slovar.popitem()
# print(slovar)
# print("Список ключей", slovar.keys())
# print("Список значений", slovar.values())


player = {
    "Имя": "John",
    "Здоровье": 100,
    "Уровень": 1,
    "Мана": 100,
    "Урон" : 25,
    "Защита" : 10
}

for key in player:
    print(f"{key}, {player[key]}")

print(" ")

enemy = {
    "Имя": "Nhoj",
    "Здоровье": 100,
    "Уровень": 1,
    "Мана": 100,
    "Урон" : 25,
    "Защита" : 10
}

for key in enemy:
    print(f"{key} : {enemy[key]}")


import time

import random

while True:
    if player["Здоровье"] <= 0:
        print("Мы проиграли")
        break
    elif enemy["Здоровье"] <= 0:
        print("Мы выиграли")
        break

    rand = random.randint(1,6)
    if rand == 1:
        print(f"{player["Имя"]} промахнулся")
    else:
        print(f"{enemy["Имя"]} наносит {player["Имя"]} {enemy["урон"]} урона")
        enemy["Здоровье"] -= player["урон"]

    print("\nОчередь противника\n")

    rand = random.randint(1,6)
    if rand == 1:
        print(f"{enemy["Имя"]} промахнулся")
    else:
        print(f"{enemy["Имя"]} наносит {player["Имя"]} {enemy["урон"]} урона")
        player["Здоровье"] -= enemy["урон"]

    print("\nОчередь Игрока\n")
    time.sleep(0.5)
print("У игрока осталось:", player["Здоровье"])
print("У игрока осталось:", enemy["Здоровье"])