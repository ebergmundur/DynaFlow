from django.contrib.auth.models import User, Group
from .models import Question, Questionnaire, QuestionGroupRelation, QuestionnaireGroupRelation,\
    Option, Category, Group as QGroup, TestMemo
from person.models import PersonUser
from rest_framework import serializers


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = [
            'id',
            'question_ref',
            'owner',
            'answer',
            'label',
            # 'option',
            # 'correct',
            # 'value_from',
            # 'value_to',
            # 'correct_value_from',
            # 'correct_value_to',
            # 'image',
            # 'selected',
            # 'checked',
            'value',
        ]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonUser
        fields = [
            'id',
            'fullname',
            'isadmin',
        ]

class QuestionMemoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestMemo
        fields = [
            'id',
            'review_date',
            'memo',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    owner = PersonSerializer(many=False)

    class Meta:
        model = Question
        fields = [
            'id',
            'name',
            'question',
            'options',
            'image',
            'owner',
            'timed',
            'time_allowed',
            'single_selection',
            'points',
            'hint_cost',
            'group_correct',
            'group_false',
            'hint',
        ]

    # def create(self, validated_data):
    #     options_data = validated_data.pop('options')
    #     question = Question.objects.create(**validated_data)
    #     for option_data in options_data:
    #         Option.objects.create(question=question, **option_data)
    #     return album


