from django.shortcuts import render
from rest_framework.views import APIView
from .models import Collects, Users
from .serializer import CollectSerializer
from django.http import JsonResponse

# Create your views here.

#todo:收藏部分有两个问题，一，查询收藏的策略时，返回的字段是超预期的。二，还没有实现正确的连表查询机制
class CollectView(APIView):

    @staticmethod
    def get(request):
        """查询我收藏的策略"""
        user_id = request.GET.get('userId')
        try:
            user_info = Users.objects.get(user_id=user_id)
            collect_info = user_info.collects
            serializer = CollectSerializer(instance=collect_info, many=True)
        except Exception as e:
            return JsonResponse({'code': '-1', 'msg': 'error', 'err_msg': f'{e}'}, safe=False)
        return JsonResponse({'code': 200, 'msg': '成功', 'result': serializer.data, 'another_result':f'{collect_info}'}, safe=False)

    def posy(self):
        pass