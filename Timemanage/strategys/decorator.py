from django.db import connection
from django.http import JsonResponse
from rest_framework import status

def check_user(fn):
    """由于策略表中的creator字段没有关联到users表,所以不存在的用户
    创建策略时，也会正常创建，这是不合理的，这个装饰器就是用于解决这个问题
    """
    def _check(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute(f"select count(*) num from users where user_id={request.POST.get('userId')}")
        user_info = cursor.fetchall()
        print(user_info)
        if user_info[0][0]:
            return fn(self, request)
        else:
            return JsonResponse({'code': status.HTTP_404_NOT_FOUND, 'err_msg': '不存在的用户信息，请重新输入'})
    return _check