years = int(input("Сколько лет смотрим на экспонаты? "))
print("Будет просмотрено " + str(years*365*96) + " экспонатов")
number_exp = int(input("Сколько экспонатов нужно осмотреть? "))
print("На просмотр уйдет " + str(number_exp//96//365) + " лет, " + str(number_exp//96) + " дней, " + str(number_exp*5) + " минут.")
