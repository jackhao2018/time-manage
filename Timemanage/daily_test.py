import py_compile

test_data = '1,2,5,7,10,15,20,25,30'.split(',')
print(test_data)
test_address = "www.narutom.com"

if a := 5 >1:
    print(f"List is too long ({a} elements, expected <= 10)")

import datetime

_CURRENT_TIME = datetime.datetime.now().strftime( '%Y-%m-%d') #  %H:%M:%S')

print(f'测试数据{_CURRENT_TIME}')

from datetime import date, timedelta

today = date.today()
d2 = today + timedelta(2)
# x = r"C:\Users\chenhao1_vendor\PycharmProjects\time-manage\Timemanage\daily_test.py"
#
# py_compile.compile(file=x, cfile=r"./test.pyc", optimize=-1)
# # compileall.compile_dir()
# print(d2)