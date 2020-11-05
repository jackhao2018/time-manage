from django.shortcuts import render
from django.http.multipartparser import MultiPartParser
from django.utils.decorators import method_decorator
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Plans, PolicyDetails
from strategys.models import Strategys
from common.decorator import check_user
from .serializer import PlanSerializer, PolicyDetailsSerializer
from django.db import connection

@method_decorator(check_user, name='dispatch')
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
        'user_id': request.POST.get('userId'),
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
        print(f'request.data包含的数据内容：{request.data}, request.query_params包含的数据内容：{request.query_params}')
        # data_dic_1 = request.data
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


@method_decorator(check_user, name='dispatch')
class PolicyDetailsView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        user_id = request.GET.get('userId')
        plan_id = request.GET.get('planId')
        strategy_id = request.GET.get('strategyId')

        try:
            policy_details_info = PolicyDetails.objects.filter(user_id=user_id, strategy_id=strategy_id, plan_id=plan_id)
            # print(policy_details_info.query)
            serializer = PolicyDetailsSerializer(instance=policy_details_info, many=True)

        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '成功', 'result': serializer.data}, safe=False)

#todo:这里预期是希望使用Django原生的ORM，但是实际使用过程中处理外键关联时有好几处坑需要处理，所以现在暂时先使用原生的SQL完成业务
    @staticmethod
    def post(request, *args, **kwargs):
        """
        用于生成执行细节时间数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data_dic = {
            'user_id': request.POST.get('userId'),
            'plan_id': request.POST.get('planId'),
            'strategy_id': request.POST.get('strategyId'),
            'execution_time': request.POST.get('executionTime'),
            'execution_time_description': request.POST.get('description'),
            'remarks': request.POST.get('remarks'),
        }
        strategy_details = Strategys.objects.values('strategy_details').filter(strategy_id=data_dic['strategy_id'])

        details_list = strategy_details[0]['strategy_details'].split(',')

        from datetime import date, timedelta

        today = date.today()

        for i in details_list :

            d2 = today + timedelta(int(i))

            data_dic['execution_time'] = d2.isoformat()

            cursor = connection.cursor()
            # print(f"INSERT INTO qianye.policy_details (user_id, plan_id, strategy_id, execution_time, execution_time_description, remarks) VALUES ({data_dic['user_id']}, {data_dic['plan_id']}, {data_dic['strategy_id']}, '{data_dic['execution_time']}', '不说', ' 测试')")
            try:
                cursor.execute(f"INSERT INTO qianye.policy_details (user_id, plan_id, strategy_id, execution_time, execution_time_description, remarks)  VALUES ({data_dic['user_id']}, {data_dic['plan_id']}, {data_dic['strategy_id']}, '{data_dic['execution_time']}', '不说', ' 测试')")
            except Exception as e:
                return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
            else:
                pass

        return JsonResponse({'code': status.HTTP_200_OK, 'msg': '计划执行时间已生成'}, safe=False)

    @staticmethod
    def put(request, *args, **kwargs):
        put = request.data
        # print(data)
        # put = MultiPartParser(request.META, request, request.upload_handlers).parse()[0]
        data_dict = {'plan_id': put['planId'], 'user_id': put['userId'], 'execution_time_old': put['OldExecutionTime'], 'execution_time_new': put['NewExecutionTime'],
                     'strategy_id': put['strategyId'], 'description': put['description'],
                     'remarks':put['remarks']
                     }
        print(data_dict)
        cursor = connection.cursor()
        try:
            # update_obj = PolicyDetails.objects.get(plan_id=data_dict['plan_id'], user_id=data_dict['user_id'], strategy_id=data_dict['strategy_id'], execution_time=data_dict['execution_time'])
            # serializer =PolicyDetailsSerializer(instance=update_obj, data=data_dict)  # ValueError: Cannot assign "1": "PolicyDetails.user_id" must be a "Users" instance.
            cursor.execute(f"UPDATE qianye.policy_details t SET t.execution_time_description = \'{data_dict['description']}\', t.remarks = \'{data_dict['remarks']}\', t.execution_time= \'{data_dict['execution_time_new']}\' WHERE t.user_id = \'{data_dict['user_id']}\' AND t.plan_id = \'{data_dict['plan_id']}\' AND t.strategy_id = \'{data_dict['strategy_id']}\' AND t.execution_time = \'{data_dict['execution_time_old']}\'")

        except Exception as e:
            return JsonResponse({'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'err_msg': f'{e}'})
        else:
            # if serializer.is_valid(raise_exception=True):
            #     serializer.save()
            return JsonResponse({'code': status.HTTP_200_OK, 'msg': '执行细节更新成功', 'saveinfo': 'serializer.data'})