from datetime import datetime

born = datetime.strptime('2019-10-10', '%Y-%m-%d')

def age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

print(age(born))