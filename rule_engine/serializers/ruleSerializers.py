from ..models.ruleModels import *
from rest_framework import serializers


class RuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rules
        exclude = ("created_at", "updated_at")

    def create(self, validated_data, exclude=None):
        return Rules.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rule_name = validated_data.get('rule_name', instance.rule_name)
        instance.signal = validated_data.get('signal', instance.signal)
        instance.value = validated_data.get('value', instance.value)
        instance.value_type = validated_data.get('value_type', instance.value_type)
        instance.criteria = validated_data.get('criteria', instance.criteria)
        instance.save()
        return instance


