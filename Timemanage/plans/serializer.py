from rest_framework import serializers
from .models import Plans

class PlanSerializer(serializers.ModelSerializer):

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
        elif begin_time < end_time:
            raise serializers.ValidationError('计划结束时间不能小与开始时间')

        return attrs
