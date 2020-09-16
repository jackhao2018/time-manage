from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import StrategySerializer
from django.http import JsonResponse
# Create your views here.

class StrategysView(APIView):
    """
    post: 为用户新增策略
    """

    def get(self):
        pass

    @staticmethod
    def post(request):
        data_dic = {
            'userId': request.POST.get('userId'),
            'strategyName': request.POST.get('strategyName'),
            'strategyDetails': request.POST.get('strategyDetails'),
            'remarks': request.POST.get('remarks'),
        }
        serializer = StrategySerializer(data=data_dic)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse(serializer.data)