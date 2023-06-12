import datetime

def get_birthdays_per_week(users):
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i in range(7):
        target_date = next_week + datetime.timedelta(days=i)
        target_weekday = weekdays[target_date.weekday()]
        birthday_users = [user['name'] for user in users if user['birthday'].month == target_date.month and user['birthday'].day == target_date.day]

        if len(birthday_users) > 0:
            print(f"{target_weekday}: {', '.join(birthday_users)}")


users = []
print("Введіть дані про користувачів та їх дні народження. Для завершення введіть 'q'.")

while True:
    name = input("Введіть ім'я користувача(або q для виходу): ")
    if name.lower() == 'q':
        break

    birthday_str = input("Введіть дату народження у форматі (день.місяць.рік): ")
    if birthday_str.lower() == 'q':
        break

    try:
        birthday = datetime.datetime.strptime(birthday_str, '%d.%m.%Y').date()
        users.append({'name': name, 'birthday': birthday})
        print("Дані додано до списку користувачів.")
    except ValueError:
        print("Некоректний формат дати. Будь ласка, спробуйте ще раз.")


print("\nСписок іменинників наступного тижня:")
get_birthdays_per_week(users)
