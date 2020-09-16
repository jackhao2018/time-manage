from rest_framework import serializers
from .models import Strategys

class StrategySerializer(serializers.ModelSerializer):

    # 这里是字段级的一级校验
    strategy_id = serializers.IntegerField(required=True)
    creator = serializers.IntegerField(required=True)
    strategy_name = serializers.CharField(required=True, max_length=255)
    strategy_details = serializers.CharField(required=True, max_length=255)

    class Meta:
        model = Strategys
        fields = '__all__'


    # 这里给入参字段自定义一些校验，并且定义返回信息
    @staticmethod
    def vaildated_strategy_name(data):
        if data is None:
            assert '用户名不能为空'

    def validate(self, attrs):
        strategy_name = attrs.get('strategyName')
        strategy_details = attrs.get('strategyDetails')

        if strategy_name or strategy_details is None:
            assert '策略名或策略细节不能为空！'
        return attrs

    #
    def create(self, validated_data):
        """数据校验成功时，为数据提供新增的方式"""
        strategy_name = validated_data.get('strategyName')
        user_id = validated_data.get('userId')
        strategy_details = validated_data.get('strategyDetails')
        remarks = validated_data.get('remarks')
        instance = Strategys.objects.create(strategy_name=strategy_name, creator=user_id,strategy_details=strategy_details, remarks=remarks)
        return instance

