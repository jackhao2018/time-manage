from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .serializer import StrategySerializer
from django.http import JsonResponse
from .models import Strategys
from rest_framework import status
from common.commom_api import GetStrategyDedail

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
        from_field = request.GET.get('from_field')

        try:
            if from_field is not None:
                strategy_info = Strategys.objects.filter(creator=creator, from_field=2)
                serializer = StrategySerializer(instance=strategy_info, many=True)
            else:
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

        if int(data_dic['customize']) == 1:
            if int(data_dic['mode']) == 0:
                data_dic['strategy_details'] = ','.join([str(x) for x in GetStrategyDedail(data_dic['begin_time'],
                                                                                           data_dic[
                                                                                               'end_time']).make_date_from_list(
                    int(data_dic['num']), mode='day')])
            elif int(data_dic['mode']) == 1:
                data_dic['strategy_details'] = ','.join([str(x) for x in GetStrategyDedail(data_dic['begin_time'],
                                                                                           data_dic[
                                                                                               'end_time']).make_date_from_list(
                    data_dic['num'], int(data_dic['interval']), mode='week')])
            elif int(data_dic['mode']) == 2:
                data_dic['strategy_details'] = ','.join([str(x) for x in GetStrategyDedail(data_dic['begin_time'],
                                                                                           data_dic['end_time']).make_date_from_list(
                    int(data_dic['num']), mode='month')])

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
        if data_dic['strategy_details']:
            pass
        else:
            if int(data_dic['customize']) == 1:
                if int(data_dic['mode']) == 0:
                    data_dic['strategy_details'] = ','.join([str(x) for x in GetStrategyDedail(data_dic['begin_time'],
                                                                     data_dic['end_time']).make_date_from_list(int(
                        data_dic['num']), mode='day')])
                elif int(data_dic['mode']) == 1:
                    data_dic['strategy_details'] = ','.join([str(x) for x in GetStrategyDedail(data_dic['begin_time'],
                                                                     data_dic['end_time']).make_date_from_list(
                        data_dic['num'], int(data_dic['interval']), mode='week')])
                elif int(data_dic['mode']) == 2:
                    data_dic['strategy_details'] = ','.join([str(x) for x in GetStrategyDedail(data_dic['begin_time'],
                                                                     data_dic['end_time']).make_date_from_list(
                        int(data_dic['num']), mode='month')])

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
            if f'{e}'.find('Cannot delete or update a parent row'):
                err_msg = '策略已被使用，请先删除使用该策略的计划'
                return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': err_msg})
            else:
                return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功删除策略:{}'})