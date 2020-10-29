from django.shortcuts import render
from django.http.multipartparser import MultiPartParser
from django.utils.decorators import method_decorator
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Plans
from common.decorator import check_user
from .serializer import PlanSerializer

@method_decorator(check_user, name='get')
class PlansView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        user_id = request.GET.get('userId')

        try:
            plan_info = Plans.objects.filter(user_id=user_id)

            serializer = PlanSerializer(instance=plan_info, many=True)
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data}, safe=False)

    @staticmethod
    def post(request, *args, **kwargs):
        data_dic = {
        'user_id': request.GET.get('userId'),
        'current_time': request.POST.get('currentTime'),
        'plan_name' : request.POST.get('planName'),
        'begin_time' : request.POST.get('beginTime'),
        'end_time' : request.POST.get('endTime'),
        'remarks' : request.POST.get('remarks'),
        'status' : request.POST.get('status'),
        'level' : request.POST.get('level'),
        'plan_type' : request.POST.get('plan_type'),
        'strategy_id' : request.POST.get('strategyId') if request.POST.get('strategyId') is None else None
        }

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
        put = MultiPartParser(request.META, request, request.upload_handlers).parse()
        data_dict = {'plan_id': put[0]['planId'], 'user_id': put[0]['userId'], 'plan_name': put[0]['planName'],
                     'strategy_id': put[0]['strategyId'], 'current_time': put[0]['currentTime'], 'begin_time': put[0]['beginTime'],
                     'end_time': put[0]['endTime'], 'status': put[0]['status'], 'remarks': put[0]['remarks'],
                     'level': put[0]['level'], 'plan_type': put[0]['planType']
                     }
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
        plan_id = args[0]
        Plans.objects.filter(plan_id=plan_id).delete()
        return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功删除计划:{}'})