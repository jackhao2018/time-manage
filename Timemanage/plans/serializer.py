from rest_framework import serializers
from .models import Plans
import datetime

_CURRENT_TIME = datetime.datetime.now()

class PlanSerializer(serializers.ModelSerializer):

    # user = serializers.IntegerField()
    # user_id = serializers.IntegerField()
    plan_name = serializers.CharField(required=True, max_length=255)
    begin_time = serializers.DateTimeField(required=True)
    end_time = serializers.DateTimeField(required=True)

    class Meta:
        model = Plans
        fields = '__all__'

    @staticmethod
    def validate_plan_name(data):
        # print('data数据：{}'.format(data))
        if data is None:
            raise serializers.ValidationError('计划名不能为空')
        return data

    def validate(self, attrs):
        print(f'{attrs}')
        current_time = attrs.get('current_time')
        begin_time = attrs.get('begin_time')
        end_time = attrs.get('end_time')

        if current_time > begin_time:
            raise  serializers.ValidationError('计划开始时间不能小与当前时间')
        elif begin_time > end_time:
            raise serializers.ValidationError('计划结束时间不能小与开始时间')

        return attrs

    def create(self, data):
        """数据校验成功时，为数据提供新增的方式"""
        # plan_id = data.get('plan_id')
        plan_name = data.get('plan_name')
        current_time = _CURRENT_TIME
        begin_time = data.get('begin_time')
        end_time = data.get('end_time')
        strategy_id = data.get('strategy_id')
        user_id = data.get('user_id')
        status = data.get('status')
        remarks = data.get('remarks')
        level = data.get('level')
        plan_type = data.get('plan_type')
        instance = Plans.objects.create(user_id=user_id, strategy_id=strategy_id, plan_name=plan_name,
                                        plan_type=plan_type, current_time=current_time, begin_time=begin_time,
                                        end_time=end_time, status=status, remarks=remarks, level=level)
        print(f'sql:信息：{instance}')
        return instance

    def update(self, instance, data):
        """数据更新时，提供update操作"""
        strategy_id = data.get('strategy_id')
        user_id = data.get('user_id')
        # plan_id = data.get('plan_id')
        plan_name = data.get('plan_name')
        current_time = _CURRENT_TIME
        begin_time = data.get('begin_time')
        end_time = data.get('end_time')
        status = data.get('status')
        remarks = data.get('remarks')
        level = data.get('level')
        plan_type = data.get('plan_type')

        instance.plan_name = plan_name
        instance.current_time = current_time
        instance.begin_time = begin_time
        instance.end_time = end_time
        instance.status = status
        instance.remarks = remarks
        instance.level = level
        instance.strategy_id = strategy_id
        instance.user_id = user_id
        instance.plan_type = plan_type
        # instance.plan_id = plan_id

        print(f'sql:信息222：{instance}')
        instance.save()

        return instance
