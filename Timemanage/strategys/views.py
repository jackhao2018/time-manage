from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import StrategySerializer
from django.http import JsonResponse
from .models import Strategys

# Create your views here.


class StrategysView(APIView):
    """
    post: 为用户新增策略
    """

    @staticmethod
    def get(request):
        """
        默认查询与用户关联的说有策略，档model为1时，则查询收藏的策略
        :return:
        """
        user_id = request.GET.get('userId')
        strategy_info = Strategys.objects.filter(creator=user_id)
        serializer = StrategySerializer(instance=strategy_info, many=True)
        return JsonResponse({'code': 200, 'msg': '成功', 'result': serializer.data}, safe=False)

    @staticmethod
    def post(request):
        data_dic = {
            'creator': request.POST.get('userId'),
            'strategy_name': request.POST.get('strategyName'),
            'strategy_details': request.POST.get('strategyDetails'),
            'remarks': request.POST.get('remarks'),
        }
        serializer = StrategySerializer(data=data_dic)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse({'code': 200, 'msg': '成功', 'result': serializer.data}, status=200)