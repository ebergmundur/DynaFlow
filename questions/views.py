from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import OptionSerializer, QuestionSerializer, QuestionMemoSerializer, QuestionAnswerSerializer, \
    GroupSerializer, CategorySerializer, QuestionnaireSerializer
from .models import Option, Question, Questionnaire, QuestionGroupRelation, QuestionnaireGroupRelation, Group, Category, \
    TestMemo, TestAnswers, QuestionnaireResults


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
    """
    List all code snippets, or create a new snippet.
    """
    # if request.method == 'GET':
    #     memos = TestMemo.objects.filter(curr_question=request)
    #     serializer = QuestionMemoSerializer(memos, many=True)
    #     return Response(serializer.data)

    if request.method == 'POST':
        serializer = QuestionMemoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            corr_opts = Option.objects.filter(id__in=cq[0].options,correct=True).count()
            print(corr_opts)

            points_per_correct = total_points/corr_opts

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
                    corrects = corrects - round(total_points/corr_opts)
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

        i = 0 # index of array refers to Category id
        for q in data['question_collection']:
            # print(q)
            if q != None:
                category = Category.objects.get(id=i)
                # print(category)
                questions = category.question.all().order_by('?')
                # print(questions)
                quest_counter = 0
                user_knows = False
                for quest in questions:
                    user_knows = False
                    if obj.omit_known:
                        memos = TestMemo.objects.filter(tesing_user_id=1, curr_question=quest.id)
                        if len(memos) > 0:
                            for m in memos:
                                if m.known:
                                    user_knows = True
                    if user_knows == False:
                        obj.question_collection.add(quest)
                        quest_counter = + 1

                    failed = True
                    if obj.only_failed:
                        previous_results = QuestionnaireResults.objects.filter(
                            user_id=1, question=quest.id).order_by('-result_date')
                        if len(previous_results) > 0:
                            for p in previous_results:
                                print('p.result',p.result )
                                if p.result == 1:
                                    failed = False
                                    break
                                else:
                                    obj.question_collection.add(quest)
                                    quest_counter = + 1

                    if quest_counter > q:
                        break

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
            corr_opts = Option.objects.filter(id__in=cq[0].options,correct=True).count()
            print(corr_opts)

            points_per_correct = total_points/corr_opts

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
                    corrects = corrects - round(total_points/corr_opts)
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