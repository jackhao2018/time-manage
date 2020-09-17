from django.shortcuts import render
from rest_framework.views import APIView
from .models import Collects
from django.http import JsonResponse

# Create your views here.


class CollectView(APIView):

    @staticmethod
    def get(request):
        """查询我收藏的策略"""
        user_id = request.GET.get('userId')
        collect_info = Collects.objects.filter(user_id=user_id)
        return JsonResponse({'code': 200, 'msg': '成功', 'result': '{}'.format(collect_info)}, safe=False)

    def posy(self):
        pass