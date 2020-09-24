from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .serializer import StrategySerializer
from django.http import JsonResponse
from .models import Strategys
from rest_framework import status
from .. import decorator
# Create your views here.

@method_decorator(check_user, name='dispatch')
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
        if user_id:
            try:
                strategy_info = Strategys.objects.filter(creator=user_id)
                serializer = StrategySerializer(instance=strategy_info, many=True)
            except Exception as e:
                return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
            else:
                return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data}, safe=False)
        else:
            return JsonResponse({'code': status.HTTP_204_NO_CONTENT, 'err_msg': '用户名不能为空！'})

    def post(self, request):
        data_dic = {
            'creator': request.POST.get('userId'),
            'strategy_name': request.POST.get('strategyName'),
            'strategy_details': request.POST.get('strategyDetails'),
            'remarks': request.POST.get('remarks'),
        }
        print(data_dic)
        try:
            serializer = StrategySerializer(data=data_dic)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            print('不会走这里？')
            print(serializer.data)
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data})