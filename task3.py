seasons_list = ['Зима', 'Осень', 'Лето', 'Весна']

seasons_dict = {

	1: 'Зима',
	2: 'Осень',
	3: 'Лето',
	4: 'Весна'
}

month = int(input("Введите месяц: "))

if month == 1 or month == 12 or month == 2:
        print(seasons_dict[1])
        print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict[2])
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict[3])
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict[4])
    print(seasons_list[3])

else:
        print("Такого месяца не существует") 