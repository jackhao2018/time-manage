from django.db import connection
from django.http import JsonResponse

def check_user(fn):
    """用于校验用户是否存在于数据库中"""
    def _check(request, *args, **kwargs):
        cursor = connection.cursor()
        user_info = cursor.execute(f"select count(*) num from users where user_id={request.POST.get('userId')}")
        print(user_info)
        if user_info:
            return fn(request)
        else:
            raise JsonResponse({'err_msg': '不存在的用户信息，请重新输入'})
    return _check