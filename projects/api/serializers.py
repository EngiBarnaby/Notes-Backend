from rest_framework import serializers

from ..models import Project, Step, TestRecursion

class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class TestRecursionSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = TestRecursion
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    count_completed_steps = serializers.SerializerMethodField("get_count_completed_steps")
    percent_of_completed = serializers.SerializerMethodField("get_percent")

    class Meta:
        model = Project
        fields = "__all__"

    def get_count_completed_steps(self, obj):
        all_steps = obj.step_set.all().count()
        steps_is_done = obj.step_set.filter(completed=True).count()
        return '{} of {}'.format(steps_is_done, all_steps)

    def get_percent(self, obj):
        all_steps = obj.step_set.all().count()
        steps_is_done = obj.step_set.filter(completed=True).count()
        if all_steps != 0:
            return (steps_is_done * 100) / all_steps
        else:
            return 0

class StepSerializer(serializers.ModelSerializer):
    sub_steps = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Step
        fields = "__all__"

    def create(self, validated_data):
        project = validated_data.pop("project")
        project = Project.objects.get(id=project.id)
        step = Step.objects.create(project=project,  **validated_data)
        return step
