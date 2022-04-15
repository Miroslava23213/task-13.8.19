number_of_tickets = int(input("Количество билетов: "))
cost_of_tickets = 0
print("Укажите возраст посетителя: ")
for i in range(number_of_tickets) :
    age = int(input("Возраст посетителя: "))
    if age < 18:
        cost_of_tickets += 0
        print("Бесплатно")
    elif 18 <= age < 25:
        cost_of_tickets += 990
        print("Стоимость билета 990 руб.")
    else:
        cost_of_tickets += 1390
        print("Стоимость билета 1390 руб.")
if number_of_tickets > 3:
    cost_of_tickets = cost_of_tickets * 0.9
    print("Стоимость билета с учётом скидки 10% для >3 людей: ", cost_of_tickets)
else:
    print("Сумма к оплате: ", cost_of_tickets)
