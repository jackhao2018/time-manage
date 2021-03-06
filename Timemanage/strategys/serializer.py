from rest_framework import serializers
from .models import Strategys


class StrategySerializer(serializers.ModelSerializer):

    # 这里是字段级的一级校验,且序列化的字段必须与表字段一致
    creator = serializers.IntegerField(required=True)
    strategy_name = serializers.CharField(required=True, max_length=255)
    strategy_details = serializers.CharField(required=True, max_length=255)

    class Meta:
        model = Strategys
        fields = '__all__'


    # 这里给入参字段自定义一些校验，并且定义返回信息
    @staticmethod
    def validate_strategy_name(data):
        print('data数据：{}'.format(data))
        if data is None:
            raise serializers.ValidationError('策略名不能为空')
        return data



    def validate(self, attrs):
        print(f'{attrs}')
        strategy_name = attrs.get('strategy_name')
        strategy_details = attrs.get('strategy_details')
        print(f'{strategy_name}---{strategy_details}')

        if strategy_name is None or strategy_details is None:
            raise serializers.ValidationError('策略名或策略细节不能为空！')
        return attrs

    #这里定义策略新增时用到的额create方法
    def create(self, data):
        """数据校验成功时，为数据提供新增的方式"""
        strategy_name = data.get('strategy_name')
        user_id = data.get('creator')
        strategy_details = data.get('strategy_details')
        remarks = data.get('remarks')
        instance = Strategys.objects.create(creator=user_id, strategy_name=strategy_name, strategy_details=strategy_details, remarks=remarks)
        return instance

    def update(self, instance, data):
        """数据更新时，提供update操作"""
        creator = data.get('creator')
        strategy_name = data.get('strategy_name')
        strategy_details = data.get('strategy_details')
        remarks = data.get('remarks')

        instance.creator = creator
        instance.strategy_name = strategy_name
        instance.strategy_details = strategy_details
        instance.remarks = remarks
        instance.save()
        return instance