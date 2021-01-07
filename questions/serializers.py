from django.contrib.auth.models import User, Group
from .models import Question, Questionnaire, QuestionGroupRelation, QuestionnaireGroupRelation, \
    Option, Category, Group as QGroup, TestMemo, TestAnswers
from person.models import PersonUser
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name',)
        extra_kwargs = {'user__password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        name = validated_data.pop('first_name')
        name = name.split( ' ')

        user = User(**validated_data)
        user.set_password(password)
        user.email = validated_data.pop('email')
        user.first_name = name[0]
        user.last_name = name[1]
        user.save()

        new_person = PersonUser.objects.create(
                user = user
        )
        new_person.save()

        return user

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
            'first_name',
            'last_name',
            'username',
            'isadmin',
            'email',
            'open',
            'until',
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
            'question',
            'known',
            'difficulty',
            'memo',
        ]


# class QuestionnaireResultsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = QuestionnaireResults
#         fields = [
#             'id',
#             'user',
#             'questionnaire',
#             'question',
#             'result',
#             'result_date',
#         ]

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    memos = QuestionMemoSerializer(many=True)
    owner = PersonSerializer(many=False)

    class Meta:
        model = Question
        fields = [
            'id',
            'name',
            'virtname',
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
            # 'group_correct',
            # 'group_false',
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
            'results',
            'final_results',
            'only_failed',
            'question_collection',
            'question_collection_str',
            'q_count',
            'created_date',
        ]


class DashboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questionnaire
        fields = [
            'id',
            'owner',
            'name',
            'timed',
            'time_allowed',
            'omit_known',
            'results',
            'final_results',
            'only_failed',
            # 'question_collection_str',
            'q_count',
            'created_date',
        ]


class QuestionAnswerSerializer(serializers.ModelSerializer):
    # tesing_user = PersonSerializer(many=False)
    question = QuestionSerializer(many=False)

    class Meta:
        model = TestAnswers
        fields = [
            'id',
            'created_date',
            'points',
            'points_given',
            'curr_question',
            'question',
            'result',
            'result_date',
            'options_ids',
        ]


class RevieweSerializer(serializers.ModelSerializer):
    # questions = QuestionSerializer(many=True)
    answers = QuestionAnswerSerializer(many=True)

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
            # 'questions',
            'answers',
            'question_collection_str',
            'q_count',
            'created_date',
        ]


