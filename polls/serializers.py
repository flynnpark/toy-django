from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from .models import Question, Choice


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class QuestionSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'owner', 'choices')

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question
