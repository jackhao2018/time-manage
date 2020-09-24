from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Collects, Users
from .serializer import CollectSerializer
from django.http import JsonResponse
from django.db import connection

# Create your views here.

#todo:收藏部分有两个问题，一，查询收藏的策略时，返回的字段是超预期的。二，还没有实现正确的连表查询机制
class CollectView(APIView):

    #todo:由于涉及到了多表联查,这里暂时使用的原生sql后续再优化成ORM模式
    @staticmethod
    def get(request):
        """查询我收藏的策略"""
        _SQL = """SELECT
	A.strategy_id,
	C.user_name,
	B.strategy_name,
	B.strategy_details,
	B.remarks 
FROM
	collects A,
	strategys B,
	users C 
WHERE
	A.strategy_id = B.strategy_id 
	AND A.user_id = {} 
	AND B.creator = C.user_id"""
        user_id = request.GET.get('userId')
        try:
            cursor = connection.cursor()
            cursor.execute(_SQL.format(user_id))
            data = cursor.fetchall()
        except Exception as e:
            return JsonResponse({'code': '-1', 'msg': 'error', 'err_msg': f'{e}'}, safe=False)
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': data}, safe=False)

    def post(self):
        pass