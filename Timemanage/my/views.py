from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from django.db import connection
from django.utils.decorators import method_decorator
from common.decorator import check_user
from .serializer import CollectSerializer

@method_decorator(check_user, name='dispatch')
class CollectView(APIView):

    #todo:由于涉及到了多表联查,这里暂时使用的原生sql后续再优化成ORM模式

    @staticmethod
    def get(request):
        """查询我收藏的策略"""
        _SQL = """select a.strategy_id, c.user_name, b.strategy_name, b.strategy_details, b.remarks from collects a, 
        strategys b, users c WHERE a.user_id=c.user_id and a.strategy_id=b.strategy_id and a.user_id={}"""

        user_id = request.GET.get('user_id')

        try:
            cursor = connection.cursor()
            cursor.execute(_SQL.format(user_id))
            data = cursor.fetchall()
        except Exception as e:
            return JsonResponse({'code': '-1', 'msg': 'error', 'err_msg': f'{e}'}, safe=False)
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': data}, safe=False)

    @staticmethod
    def post(request, *args, **kwargs):
        data_dic = request.data

        try:
            serializer = CollectSerializer(data=data_dic)
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data})