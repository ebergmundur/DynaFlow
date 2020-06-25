from django.contrib.auth.models import User, Group
from .models import Question, Questionnaire, QuestionGroupRelation, QuestionnaireGroupRelation,\
    Option, Category, Group as QGroup
from rest_framework import serializers


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = [
            'question_ref',
            'owner',
            'answer',
            'correct',
            'value_from',
            'value_to',
            'correct_value_from',
            'correct_value_to',
            'image',

        ]


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'question',
            'image',
            'owner',
            'timed',
            'time_allowed',
            'single_selection',
            'points',
            'hint_cost',
            'group_correct',
            'group_false',
            'options',

        ]

