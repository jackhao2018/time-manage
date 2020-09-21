from rest_framework import serializers
from .models import Collects


class CollectSerializer(serializers.ModelSerializer):

    strategy_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = Collects
        fields = '__all__'

        # 这里定义策略新增时用到的额create方法
    def create(self, validated_data):
        """数据校验成功时，为数据提供新增的方式"""
        strategy_id = validated_data.get('strategy_id')
        user_id = validated_data.get('user_id')
        instance = Collects.objects.create(user_id=user_id, strategy_id=strategy_id)
        return instance

    def update(self, instance, validated_data):
        """数据更新时，提供update操作"""
        strategy_id = validated_data.get('strategy_id')
        user_id = validated_data.get('user_id')
        instance.strategy_id = strategy_id
        instance.user_id = user_id
        instance.save()
        return instance

