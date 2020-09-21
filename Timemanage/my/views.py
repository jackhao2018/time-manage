from django.shortcuts import render
from rest_framework.views import APIView
from .models import Collects
from .serializer import CollectSerializer
from django.http import JsonResponse

# Create your views here.


class CollectView(APIView):

    @staticmethod
    def get(request):
        """查询我收藏的策略"""
        user_id = request.GET.get('userId')
        try:
            collect_info = Collects.objects.filter(user_id=user_id)
            serializer = CollectSerializer(instance=collect_info, many=True)
        except Exception as e:
            return JsonResponse({'code': '-1', 'msg': 'error', 'err_msg': f'{e}'}, safe=False)
        return JsonResponse({'code': 200, 'msg': '成功', 'result': serializer.data, 'another_result':f'{collect_info}'}, safe=False)

    def posy(self):
        pass