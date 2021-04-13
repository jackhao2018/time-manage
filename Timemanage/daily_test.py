from datetime import date, datetime


_CURRENT_TIME = date.today()

if _CURRENT_TIME > datetime.strptime('2021-04-12', '%Y-%m-%d').date():
    print('这样阔以比较')

