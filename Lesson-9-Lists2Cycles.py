# ---------------------------------- #
#   Writen by Stanislav Politikin    #
#                                    #
#                                    #
# Version      Date      Info        #
#   1.0        2023   Init.Version   #
#                                    #
# ---------------------------------- #

#         0      1      2       3          4
cars = ['audi', 'vw', 'seat', 'skoda', 'porsche']

for bibika in cars:
    print(bibika.upper())

"""
print("\n----------------------------------\n")
"""

for n in range(1, 10):
    print(n)

print("\n----------------------------------\n")

#Создаем массив
mynumber_list = list(range(0, 10))
print(mynumber_list) #просто посмотрим результат
print("================================")
for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is: " + str(max(mynumber_list)))
print("Max number is: " + str(min(mynumber_list)))
print("Sum of list is: " + str(sum(mynumber_list)))

print("\n----------------------------------\n")
#         0      1      2       3          4
cars = ['audi', 'vw', 'seat', 'skoda', 'porsche']

mycars = cars[1:4] #считаем от 1 до 4 (4 НЕ ВКЛЮЧИТЕЛЬНО)
print(mycars)
mycars = cars[:3] #Считаем с самого начала (0) до  3
print(mycars)
mycars = cars[-3:-1] #Считаем в обратную сторону

print("\n----------------------------------\n")
#Скопировать массив
#         0      1      2       3          4
cars = ['audi', 'vw', 'seat', 'skoda', 'porsche']
mycars = cars[:] # С [:] копируем cars и даже после изменения cars массив mycars не изменится