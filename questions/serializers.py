from django.contrib.auth.models import User, Group
from .models import Question, Questionnaire, QuestionGroupRelation, QuestionnaireGroupRelation, \
    Option, Category, Group as QGroup, TestMemo, TestAnswers, QuestionnaireResults
from person.models import PersonUser
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'q_count',
        ]

class QuestionGroupRelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionGroupRelation
        fields = [
            'id',
        ]


class GroupSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True)
    # q_count = QuestionGroupRelationSerializer(many=False)

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
        ]



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
            'correct',
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
    tesing_user = PersonSerializer(many=False)
    class Meta:
        model = TestMemo
        fields = [
            'id',
            'created_date',
            'tesing_user',
            'curr_question',
            'known',
            'difficulty',
            'memo',
        ]


class QuestionAnswerSerializer(serializers.ModelSerializer):
    # tesing_user = PersonSerializer(many=False)

    class Meta:
        model = TestAnswers
        fields = [
            'id',
            'created_date',
            # 'tesing_user',
            'time_allowed',
            'time_taken',
            'options_ids',
            'points',
            'curr_question',
            'test_practice',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    memos = QuestionMemoSerializer(many=True)
    owner = PersonSerializer(many=False)

    class Meta:
        model = Question
        fields = [
            'id',
            'name',
            'question',
            'description',
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
            'memos'
        ]

    # def create(self, validated_data):
    #     options_data = validated_data.pop('options')
    #     question = Question.objects.create(**validated_data)
    #     for option_data in options_data:
    #         Option.objects.create(question=question, **option_data)
    #     return album


class QuestionnaireSerializer(serializers.ModelSerializer):
    question_collection = QuestionSerializer(many=True)

    class Meta:
        model = Questionnaire
        fields = [
            'id',
            'owner',
            'name',
            'timed',
            'time_allowed',
            'omit_known',
            'only_failed',
            'question_collection',
            'question_collection_str',
            'q_count',
        ]

    # def save(self):
    #     print(self.validated_data)
    #     q_coll = collect_questions(self.validated_data['question_collection'])
    #     # owner = 1
    #     # timed = self.validated_data['timed']
    #     # time_allowed = self.validated_data['time_allowed']
    #     # omit_known = self.validated_data['omit_known']
    #     # question_collection_str = self.validated_data['question_collection_str']

class QuestionnaireResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionnaireResults
        fields = [
            'id',
            'user',
            'questionnaire',
            'question',
            'result',
            'result_date',
        ]