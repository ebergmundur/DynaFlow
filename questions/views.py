from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import OptionSerializer, QuestionSerializer, QuestionMemoSerializer, QuestionAnswerSerializer, \
    GroupSerializer, CategorySerializer, QuestionnaireSerializer, RevieweSerializer
from .models import Option, Question, Questionnaire, QuestionGroupRelation, QuestionnaireGroupRelation, Group, Category, \
    TestMemo, TestAnswers


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('?')
    serializer_class = QuestionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Option.objects.all().order_by('?')
    serializer_class = OptionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionnaireViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Questionnaire.objects.all().order_by('?')
    serializer_class = QuestionnaireSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Questionnaire.objects.all().order_by('?')
    serializer_class = RevieweSerializer


# class QuestionMemoViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     memo = Option.objects.all()
#     serializer_class = QuestionMemoSerializer
#
#
# class QuestionAnswerViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     memo = TestAnswers.objects.all()
#     serializer_class = QuestionAnswerSerializer


@api_view(['POST'])
def memo_add(request):

    if request.method == 'POST':
        # serializer = QuestionMemoSerializer(data=request.data)
        data = request.data

        quest = Question.objects.filter(id=data['curr_question'])

        memo = TestMemo.objects.create(
            curr_question=data['curr_question'],
            question=quest[0],
            memo=data['memo'],
            known=data['known'],
            difficulty=data['difficulty'],
        )

        memo.save()

        return Response(data, status=status.HTTP_201_CREATED)

        # if serializer.is_valid():
        #     print("serializer valid")
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print("serializer NOT valid")
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def answer_add(request):
    """
    List all code snippets, or create a new snippet.
    """
    print(request.data)

    if request.method == 'GET':
        # memos = TestAnswers.objects.filter(curr_question=request)
        memos = TestAnswers.objects.all()
        serializer = QuestionAnswerSerializer(memos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = QuestionAnswerSerializer(data=request.data)
        data = request.data

        cq = Question.objects.filter(id=data['curr_question'])
        tp = Questionnaire.objects.filter(id=data['test_practice'])
        total_points = cq[0].points

        # RESULT = [
        #     [-1, 'Failed'],
        #     [0, 'Postponed'],
        #     [1, 'Correct'],
        # ]
        points_earned = 0
        results = 0

        opt_id = None
        if data['options_ids'] > '':
            try:
                opt_id = int(data['options_ids'])
            except:
                pass

        if data['postpone'] == True:
            results = 0
            points_earned = 0
        else:
            if opt_id:
                answ = Option.objects.filter(id=opt_id)
                if answ[0].correct:
                    results = 1
                    points_earned = int(data['points'])
                else:
                    results = -1
                    points_earned = int(data['points']) * -1

        obj = TestAnswers.objects.create(
            # tesing_user=1,
            # time_allowed=data['time_allowed'],
            # time_taken=data['time_taken'],
            curr_question=cq[0].id,
            question=cq[0],
            options_ids=str(data['options_ids']),
            test_practice=tp[0],
            points=int(data['points']),
            known=data['known'],
            postpone=data['postpone'],
            points_given=points_earned,
            result=results,
        )

        obj.save()

        print(obj.points_given)
        print(obj.result)

        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def practice_test(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        # memos = TestAnswers.objects.filter(curr_question=request)
        practice = Questionnaire.objects.all()
        serializer = QuestionnaireSerializer(practice, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # serializer = QuestionnaireSerializer(data=request.data)
        data = request.data

        # print(data)
        obj = Questionnaire.objects.create(
            owner_id=1,
            timed=data['timed'],
            name=data['examname'],
            time_allowed=data['time_allowed'],
            omit_known=data['omit_known'],
            only_failed=data['only_failed'],
            question_collection_str=str(data['question_collection_str']),
        )

        i = 0  # index of array refers to Category id
        print(data['question_collection'])
        for q in data['question_collection']:
            print(q)
            if q == None:
                q = 0
            if q > 0:
                category = Category.objects.get(id=i)
                print(category.name)
                print('actual q: ', q)
                questions = category.question.all().order_by('?')
                # print(questions.count())
                quest_counter = 0
                for question in questions:
                    print('quest_counter ', quest_counter)
                    if quest_counter < q:
                        if data['omit_known'] == False and data['only_failed'] == False:
                            print('normal')
                            obj.question_collection.add(question)
                            quest_counter += 1
                        else:
                            if data['omit_known'] == True:
                                print('known')
                                answers = TestAnswers.objects.filter(
                                    tesing_user_id=1,
                                    curr_question=question.id,
                                    known=True
                                )
                                if len(answers) == 0:
                                    obj.question_collection.add(question)
                                    quest_counter += 1

                            if data['only_failed'] == True:
                                print('only_failed')
                                previous_results = TestAnswers.objects.filter(
                                    user_id=1,
                                    question=question.id,
                                    result__gt=0
                                )
                                if len(previous_results) == 0:
                                    obj.question_collection.add(question)
                                    quest_counter += 1

            i = i + 1
        ok = obj.save()

        # if serializer.is_valid():
        #     serializer.save()
        return Response(status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def practice_hand_in(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = QuestionAnswerSerializer(data=request.data)
        # print(serializer)
        data = request.data
        points = 0

        cq = Question.objects.filter(id=data['curr_question'])
        tp = Questionnaire.objects.filter(id=data['test_practice'])
        total_points = cq[0].points

        print(points)
        print(total_points)

        if cq[0].single_selection:
            answered = Option.objects.filter(id=int(data['options_ids']))
            if answered[0].correct:
                points = total_points
        else:
            i = 0
            corrects = 0
            corr_opts = Option.objects.filter(id__in=cq[0].options, correct=True).count()
            print(corr_opts)

            points_per_correct = total_points / corr_opts

            anstring = data['options_ids'].split(',')
            for answ in anstring:
                opt = Option.objects.get(id=int(answ))
                print(opt.answer)
                print(opt.correct)
                if opt.correct:
                    print('correct')
                    corrects = corrects + points_per_correct
                    print(corrects)
                else:
                    print('wrong')
                    corrects = corrects - round(total_points / corr_opts)
                    print(corrects)
                i += 1

            points = round(corrects)
            # points = round(corrects/total_points)
        print(points)

        obj = TestAnswers.objects.create(
            # tesing_user=1,
            time_allowed=data['time_allowed'],
            time_taken=data['time_taken'],
            curr_question=cq[0].id,
            options_ids=str(data['options_ids']),
            test_practice=tp[0],
            points=points,
        )

        obj.save()

        # {'time_allowed': 120, 'time_taken': 46, 'options_ids': '149,150', 'curr_question': 49, 'test_practice': 48}

        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
