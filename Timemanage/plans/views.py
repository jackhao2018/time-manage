from django.shortcuts import render

from django.utils.decorators import method_decorator
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Plans
from common.decorator import check_user
from .serializer import PlanSerializer

@method_decorator(check_user, name='dispatch')
class PlansView(APIView):

    @staticmethod
    def get(request):
        user_id = request.GET.get('userId')


        try:
            plan_info = Plans.objects.filter(user_id=user_id)
            print(f'plan_info：{plan_info}信息')
            serializer = PlanSerializer(instance=plan_info, many=True)
        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data}, safe=False)

    @staticmethod
    def post(request):
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
        'strategy_id' : request.POST.get('strategyId') if request.POST.get('strategyId') is None else 'null'
        }
        print(f'入参信息：{data_dic}')
        try:
            serializer = PlanSerializer(data=data_dic)
            # print(f'sql:{serializer}')
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except Exception as e:
            print('是这里报错了')
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data})

    def putch(self):
        pass

    def delete(self):
        pass