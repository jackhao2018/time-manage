from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Plans
from .serializer import PlanSerializer

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
        user_id = request.GET.get('userId')
        plan_name = request.POST.get('planName')
        begin_time = request.POST.get('planName')
        end_time = request.POST.get('planName')
        remarks = request.POST.get('planName')
        strategy = request.POST.get('planName') if  request.POST.get('planName') is None else 'null'

    def putch(self):
        pass

    def delete(self):
        pass