# ---------------------------------- #
#   Writen by Stanislav Politikin    #
#                                    #
#                                    #
# Version      Date      Info        #
#   1.0        2023   Init.Version   #
#                                    #
# ---------------------------------- #

#Что бы не делать так
print("****")
print("****")
print("****")
print("****")
print("\n----------------------------------\n")
#Нужно делать так
for x in range(0, 10):
    print("****")
print("\n----------------------------------\n")

#Перечисляем цикл
for n in range(0, 10 + 1):
    print(n)
print("\n\tDifference is:\n")
for n in range(0, 10):
    print(n + 1)
print("\n\tOne more:\n")
for n in range(0, 100, 10):
    print(n)
print("\n----------------------------------\n")
for n in range(-100, 10, 5):
    print("Number n = " + str(n))
    if n == 50:
        break
print("\n----------------------------------\n")

#Бесконечный цикл
loop = 0

while True:
    loop = loop + 1
    print(loop)
#прервать цикл
    if loop == 100:
        break
print("\n-------------END-------------\n")
