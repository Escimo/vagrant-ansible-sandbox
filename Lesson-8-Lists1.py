# ---------------------------------- #
#   Writen by Stanislav Politikin    #
#                                    #
#                                    #
# Version      Date      Info        #
#   1.0        2023   Init.Version   #
#                                    #
# ---------------------------------- #

cities = ['New York', 'sumy', 'Szczecin', 'Winnipeg', 'London']

print(cities)
print(len(cities)) #Выводим количество значений(длинну массива)

print(cities[0])
print(cities[-1])
print(cities[1].upper())

#Заменяем указанное значение другим
cities[2] = 'Stargard'
print(cities)

#Добавляем значение в конец списка
cities.append('Kyiv')
cities.append('Vancuver')
print(cities)

#Добавляем значение на определенную позицию
cities.insert(1, 'Los Angeles')
print(cities)

#Удаление значения из массива
del cities[2]
print(cities)
#Если не знаем номер в огромном массиве - можно использовать название
cities.remove('Winnipeg')
print(cities)

#Удаляет последнее (если не указано другое) значение и выводит сообщение.
deleted_city = cities.pop()
print("Deleted city is: " + deleted_city)
print(cities)

#Сортировка
cities.sort(reverse=False)
print(cities)
