#Snippet 1
for x in range (0,151):
    print(x)

#Snippet 2
for x in range (5,1005,5):
    print (x)

#Snippet 3
for x in range (1,101):
    if x %5 ==0:
        print("Dojo")
    elif x %10 ==0:
        print("Dojo")
    else:
        print(x)

#Snippet 4
Oddtotal = 0

for number in range(1, 500001):
    if(number % 2 != 0):
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal)) 

#Snippet 5
for x in range (2018, 0, -4):
    print (x)

#Snippet 6
for number in range(5,45):
    if(number % 7 == 0):
        print(number)

