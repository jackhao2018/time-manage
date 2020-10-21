from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .serializer import StrategySerializer
from django.http import JsonResponse
from .models import Strategys
from rest_framework import status
from common.decorator import check_user

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
        # print(f'user_id的值是：{user_id}，数据类型是{type(user_id)}')
        if user_id is not None:
            try:
                strategy_info = Strategys.objects.filter(creator=user_id)
                serializer = StrategySerializer(instance=strategy_info, many=True)
            except Exception as e:
                return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
            else:
                return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data}, safe=False)
        else:
            return JsonResponse({'code': status.HTTP_204_NO_CONTENT, 'err_msg': '请输入用户名！'})

    @staticmethod
    def post(request):
        data_dic = {
            'creator': request.POST.get('userId'),
            'strategy_name': request.POST.get('strategyName'),
            'strategy_details': request.POST.get('strategyDetails'),
            'remarks': request.POST.get('remarks'),
        }
        try:
            serializer = StrategySerializer(data=data_dic)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data})