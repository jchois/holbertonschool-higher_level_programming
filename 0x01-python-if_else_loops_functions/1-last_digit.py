import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10
if number <= 0:
    lastdig = lastdig * -1
str = "Last digit of {} is {}".format(number, lastdig)
if lastdig == 0:
    print(str + " and is 0")
elif lastdig > 5:
    print(str + " and is greater than 5")
else:
    print(str + " and is less than 6 and not 0")
