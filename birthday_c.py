from datetime import datetime, timedelta

def get_next_weekday(weekday):
    days_ahead = weekday - datetime.now().weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return datetime.now().date() + timedelta(days=days_ahead)

birthdays = {}

while True:
    name = input("Введіть ім'я (або введіть 'q' для завершення): ")
    if name.lower() == 'q':
        break
    
    birthday = input("Введіть дату народження у форматі ДД.ММ.РРРР: ")
    try:
        birthday = datetime.strptime(birthday, "%d.%m.%Y").date()
        
        next_week = get_next_weekday(0)  # Понеділок наступного тижня
        
        if birthday.weekday() >= 5:  # Якщо день народження припадає на вихідні
            next_week += timedelta(weeks=1)  # Переносяться на понеділок через два тижні
        
        if birthday >= next_week and birthday.weekday() < 5:  # Якщо день народження відповідає вимогам
            weekday = birthday.strftime('%A')
            
            if weekday not in birthdays:
                birthdays[weekday] = []
            
            birthdays[weekday].append(name)
    except ValueError:
        print("Некоректний формат дати.")

if len(birthdays) > 0:
    for weekday, names in birthdays.items():
        print(f"{weekday}: {', '.join(names)}")
else:
    print("Дні народження ще не скоро.")