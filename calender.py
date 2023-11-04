import calendar 
j= int(input('Enter the year:\n'))
for i in range (1,13):
    a= calendar.month(j, i)
    print(a)