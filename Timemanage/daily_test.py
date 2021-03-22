def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]

test_list = ['5', '6', 10, 11, 10, 20, 11]

for i in test_list:
    if i ==1:
        pass
# i = 10
# while i != 0:
#     for h in range(1, i):
#         print(f"{h}*{i-1}={h*(i-1)}", end=' ')
#     print()
#     i-=1

for l in range(10, 1, -1):
    for h in range(1, l):
        print(f"{h}*{l - 1}={h * (l - 1)}", end=' ')
    print()
