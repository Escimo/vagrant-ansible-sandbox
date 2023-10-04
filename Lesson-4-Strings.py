
# ---------------------------------- #
#   Writen by Stanislav Politikin    #
#                                    #
#                                    #
# Version      Date      Info        #
#   1.0        2023   Init.Version   #
#                                    #
# ---------------------------------- #

name = "staNIslav polItiKin"

print(name.title()) #Write string with Title Letters
print(name.upper()) #Write string with CAPITAL LETTERS

print("----------------------------------\n\n")

#Перенос текста по строкам
print("This is\ntest message\n\nwith strings")
#Перенос по строкам и отступ
print("Messages:\n\tMessage #1\n\tMessage #2\nEND")

print("----------------------------------\n\n")

#Убираем мусор из текста
a = " . , @, ! Stanislav Politikin . , 1, ?.,"
print(a.rstrip()) #убрать пробел, lstrip - слева, rstrip - справа, strip - c двух сторон
print(a.strip(" ,.@!1?")) #Перечисляем символы которые хотим убрать
