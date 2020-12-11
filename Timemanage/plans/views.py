from django.utils.decorators import method_decorator
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Plans, PolicyDetails
from strategys.models import Strategys
from common.decorator import check_user
from .serializer import PlanSerializer, PolicyDetailsSerializer

# @method_decorator(check_user, name='dispatch')
class PlansView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        user_id = request.GET.get('user_id')

        try:
            plan_info = Plans.objects.filter(user_id=user_id)

            serializer = PlanSerializer(instance=plan_info, many=True)
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data}, safe=False)

    @staticmethod
    def post(request, *args, **kwargs):

        data_dic = request.data

        try:
            serializer = PlanSerializer(data=data_dic)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data})

    @staticmethod
    def put(request, *args, **kwargs):

        data_dict = request.data

        try:
            update_obj = Plans.objects.get(plan_id=data_dict['plan_id'])
            serializer = PlanSerializer(instance=update_obj, data=data_dict)
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return JsonResponse({'code':status.HTTP_200_OK, 'msg': '保存成功', 'saveinfo': serializer.data})


#TODO:删除计划时，应该还要回显删除的计划名，后台只负责删除对应的计划，计划名由前端处理，获取后台的格式然后填充当前的计划名
    @staticmethod
    def delete(request, *args, **kwargs):  # 删除操作

        plan_id = request.data['plan_id']
        try:
            Plans.objects.get(plan_id=plan_id).delete()
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功删除计划:{}'})


@method_decorator(check_user, name='dispatch')
class PolicyDetailsView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        user_id = request.GET.get('user_id')
        plan_id = request.GET.get('plan_id')
        strategy_id = request.GET.get('strategy_id')

        try:
            policy_details_info = PolicyDetails.objects.filter(user_id=user_id, strategy_id=strategy_id, plan_id=plan_id)
            print(policy_details_info.query)
            serializer = PolicyDetailsSerializer(instance=policy_details_info, many=True)

        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data}, safe=False)

    @staticmethod
    def post(request, *args, **kwargs):
        """
        用于生成执行细节时间数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        request.POST._mutable = True   # 设置request对象可以改动

        data_dic = request.data

        strategy_details = Strategys.objects.values('strategy_details').filter(strategy_id=request.data['strategy_id'])

        details_list = strategy_details[0]['strategy_details'].split(',')

        from datetime import date, timedelta

        today = date.today()

        for i in details_list :

            d2 = today + timedelta(int(i))

            data_dic['execution_time'] = d2.isoformat()

            try:
                serializer = PolicyDetailsSerializer(data=data_dic)

            except Exception as e:
                return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
            else:
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
        return JsonResponse({'code': status.HTTP_200_OK, 'msg': '计划执行时间已生成'}, safe=False)

    @staticmethod
    def put(request, *args, **kwargs):
        data_dict = request.data
        # data_dict = json.dumps(response.renderer_context['request'].data)
        try:
            update_obj = PolicyDetails.objects.get(detail_id=data_dict['detail_id'])

            serializer =PolicyDetailsSerializer(instance=update_obj, data=data_dict)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '执行细节更新成功', 'saveinfo': serializer.data})

    @staticmethod
    def delete(request, *args, **kwargs):

        detail_id = request.data['detail_id']

        try:
            PolicyDetails.objects.get(detail_id=detail_id).delete()

        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code':status.HTTP_200_OK, 'msg': '成功删除对应的细则'})


class MDPlanView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        del_list = request.data['plan_id'].split(',')
        try:
            Plans.objects.filter(plan_id__in=del_list).delete()
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功删除计划:{}'})


class MDDetailsView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        del_list = request.data['details_id'].split(',')
        try:
            PolicyDetails.objects.filter(detail_id__in=del_list).delete()
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功删除计划:{}'})