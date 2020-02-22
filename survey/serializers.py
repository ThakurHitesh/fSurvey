from rest_framework import serializers

from .models import Question, Choice


class ChoiceSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    question_id = serializers.CharField(max_length=200)
    choice_text = serializers.CharField(max_length=200)
    created_at = serializers.CharField(read_only=True)
    votes = serializers.IntegerField()

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class ChoiceSerializerWithVotes(ChoiceSerializer):
    votes = serializers.CharField(read_only=True)


class QuestionListPageSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    question_text = serializers.CharField(max_length=200)
    created_at = serializers.CharField(read_only=True)
    pub_date = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionDetailPageSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    pub_date = serializers.CharField(read_only=True)
    question_text = serializers.CharField(max_length=200)
    choices = ChoiceSerializer(many=True, read_only=True)
