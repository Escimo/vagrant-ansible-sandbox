# ---------------------------------- #
#   Writen by Stanislav Politikin    #
#                                    #
#                                    #
# Version      Date      Info        #
#   1.0        2023   Init.Version   #
#                                    #
# ---------------------------------- #

age = 32

if age <= 4:
    print("You are baby")
elif (age > 4) and (age < 12):
    print("You are kid")
elif (age >= 12) and (age < 19):
    print("You are teenager")
else:
    print("You are old")

print("----END----")

all_cars = ['audi', 'vw', 'skoda', 'porsche', 'lambo', 'kia', 'ford', 'toyota', 'dodge']
german_cars = ['audi', 'vw', 'porsche']

for x in all_cars:
    if x in german_cars:
        print(x + " is a German car")
    else:
        print(x + " is not a German car")

print("----END----")