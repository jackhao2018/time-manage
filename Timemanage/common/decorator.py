from django.db import connection
from django.http import JsonResponse
from rest_framework import status
from my.models import Users
from django.http.multipartparser import MultiPartParser

def check_user(fn):
    """由于策略表中的creator字段没有关联到users表,所以不存在的用户
    创建策略时，也会正常创建，这是不合理的，这个装饰器就是用于解决这个问题
    """
    def _check(request, *args, **kwargs):

        if request.method in ('GET', 'POST'):
            user_id = request.GET.get('user_id') if request.method == 'GET' else request.POST.get('user_id')
        else:
            user_id = MultiPartParser(request.META, request, request.upload_handlers).parse()[0]['user_id']

        try:
            Users.objects.get(user_id=user_id)
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return fn(request, *args, **kwargs)

    return _check
