from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .serializer import StrategySerializer
from django.http import JsonResponse
from .models import Strategys
from rest_framework import status
from common.decorator import check_user

#@method_decorator(check_user, name='dispatch')
class StrategysView(APIView):
    """
    post: 为用户新增策略
    """

    @staticmethod
    def get(request, *args, **kwargs):
        """
        默认查询与用户关联的说有策略，档model为1时，则查询收藏的策略
        :return:
        """
        creator = request.GET.get('user_id')

        try:
            strategy_info = Strategys.objects.filter(creator=creator)
            serializer = StrategySerializer(instance=strategy_info, many=True)
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data}, safe=False)

    @staticmethod
    def post(request, *args, **kwargs):

        request.POST._mutable = True

        data_dic = request.data
        data_dic['creator'] = data_dic['user_id']
        del data_dic['user_id']

        try:
            serializer = StrategySerializer(data=data_dic)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data})

    @staticmethod
    def put(request, *args, **kwargs):

        request.POST._mutable = True

        data_dic = request.data

        data_dic['creator'] = data_dic['user_id']
        del data_dic['user_id']

        try:
            strategy_info = Strategys.objects.get(strategy_id=data_dic['strategy_id'])

            serializer = StrategySerializer(instance=strategy_info, data=data_dic)
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return JsonResponse({'code': status.HTTP_200_OK, 'msg': '执行细节更新成功', 'saveinfo': serializer.data})

    @staticmethod
    def delete(request, *args, **kwargs):

        strategy_id = request.data['strategy_id']
        # print(strategy_id)
        try:

            Strategys.objects.filter(strategy_id=strategy_id).update(creator=0)
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功删除策略:{}'})

class MDstrategyView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        del_list = request.data['strategy_id'].split(',')
        try:
            Strategys.objects.filter(strategy_id__in=del_list).delete()
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功删除策略:{}'})