print("Введите четырёхзначное число")
a=int(input())
if ((a//1000)==(a%10)) and ((a%1000//100)==(a%100//10)):
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
