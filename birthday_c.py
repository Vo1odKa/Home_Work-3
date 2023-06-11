from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    current_date = datetime.now().date()
    next_week_start = current_date + timedelta(days=(7 - current_date.weekday()))
    birthdays = {}
    
    for user in users:
        name = user['name']
        birthday = datetime.strptime(user['birthday'], "%d.%m.%Y").date()
        
        if birthday < next_week_start:
            weekday = birthday.strftime('%A')
            
            if weekday not in birthdays:
                birthdays[weekday] = []
            
            birthdays[weekday].append(name)
    
    for weekday, names in birthdays.items():
        print(f"{weekday}: {', '.join(names)}")


users = [
    {'name': 'Bill', 'birthday': '12.06.2023'},
    {'name': 'Jill', 'birthday': '12.06.2023'},
    {'name': 'Kim', 'birthday': '16.06.2023'},
    {'name': 'Jan', 'birthday': '16.06.2023'}
]

get_birthdays_per_week(users)