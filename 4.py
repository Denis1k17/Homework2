viewing_years = int(input("годы в течении которых посетитель будет постоянно смотреть на экспонаты"))
print("Колличество просмотренных экспонатов:", viewing_years * 365 * 8 * 60 // 5)

exhibits = int(input("Колличество экспонатов")

all_time = exhibits * 5

days = all_time // 480
all_time = days * 480

years = days // 365
days %= 365

print("years", years, "days", days, "mins", all_time)
