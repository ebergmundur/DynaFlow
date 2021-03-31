import datetime
from django.db.models.expressions import F

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from django.core.serializers import serialize

from .serializers import (
    OptionSerializer,
    QuestionSerializer,
    QuestionMemoSerializer,
    QuestionAnswerSerializer,
    GroupSerializer,
    CategorySerializer,
    QuestionnaireSerializer,
    RevieweSerializer,
    PersonSerializer,
    UserSerializer,
    DashboardSerializer,
    HeatmapSerializer,
    TextBlockSerializer,
    CatStatSerializer,
)
from .models import (
    Option,
    Question,
    Questionnaire,
    QuestionGroupRelation,
    QuestionnaireGroupRelation,
    Group,
    Category,
    TestMemo,
    TestAnswers, TextBlock,
)
from person.models import PersonUser

from rest_framework.response import Response
from rest_framework import generics


class UserCreate(generics.CreateAPIView):
    queryset = PersonUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (AllowAny, )


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Question.objects.all().order_by("?")
    serializer_class = QuestionSerializer


class FlipcardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by("?")
    serializer_class = QuestionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Option.objects.all().order_by("?")
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

    queryset = Category.objects.filter(name__gt='')
    serializer_class = CategorySerializer


class QuestionnaireViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Questionnaire.objects.all().order_by("?")
    serializer_class = QuestionnaireSerializer


class DahboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Questionnaire.objects.filter(owner_id=1).order_by("created_date")
    serializer_class = QuestionnaireSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Questionnaire.objects.filter(owner_id=1).order_by("-created_date")
    serializer_class = RevieweSerializer


@api_view(["POST"])
def dashboard(request):
    # print(request.data)
    if request.method == "POST":
        queryset = Questionnaire.objects.filter(
            owner__user__username=request.data["username"],
            answered_questions__gt=0
        ).order_by("created_date")
        # queryset = Questionnaire.objects.all().order_by('created_date')
        serializer = DashboardSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def review(request):
    qid = int(request.data["id"])
    print(request.data["username"])
    if request.method == "POST":
        if qid > 0:
            queryset = Questionnaire.objects.filter(
                owner__user__username=request.data["username"], id=qid
            )[0]
            serializer = RevieweSerializer(queryset, many=False)
            return Response(serializer.data)
        else:
            queryset = Questionnaire.objects.filter(
                owner__user__username=request.data["username"]
            ).order_by("-created_date")
            serializer = RevieweSerializer(queryset, many=True)
            return Response(serializer.data)
        


@api_view(["POST"])
def heatmap(request):
    if request.method == "POST":
        tests = Questionnaire.objects.filter(
            owner__user__username=request.data["username"]
        ).order_by("modified_date")
        serializer = HeatmapSerializer(tests, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = PersonUser.objects.all().order_by("?")
    serializer_class = PersonSerializer


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


@api_view(["GET"])
def logout(request):
    print(request)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["POST"])
def userdata(request):
    # print(request.user)
    if request.method == "POST":
        user = PersonUser.objects.filter(user__username=request.user)
        serializer = PersonSerializer(user[0], many=False)
        return Response(serializer.data)


@api_view(["POST"])
def indexcards(request):
    if request.method == "POST":
        idx_cards = TextBlock.objects.filter(spot__in=[1, 2]).order_by('spot', 'order')

        serializer = TextBlockSerializer(idx_cards, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def catstat(request):
    if request.method == "POST":
        cats = Category.objects.all()
        cat_list = []

        for c in cats:
            ta = TestAnswers.objects.filter(created_by__username=request.user,question__category=c).order_by( 'question__id').distinct('question__id').count()
            cat_list.append({'category': c, 'catcount': c.q_count(), 'answcount': ta})
        
        print(cat_list)

        serializer = CatStatSerializer(cat_list, many=True)
        return Response(serializer.data)

        


@api_view(["POST"])
def memo_add(request):
    if request.method == "POST":
        # serializer = QuestionMemoSerializer(data=request.data)
        data = request.data

        quest = Question.objects.filter(id=data["curr_question"])

        memo = TestMemo.objects.create(
            curr_question=data["curr_question"],
            question=quest[0],
            memo=data["memo"],
            known=data["known"],
            difficulty=data["difficulty"],
        )

        memo.save()

        return Response(data, status=status.HTTP_201_CREATED)

        # if serializer.is_valid():
        #     print("serializer valid")
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print("serializer NOT valid")
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def prefs(request):

    if request.method == "GET":
        # prefs = TestAnswers.objects.filter(curr_question=request)
        person = PersonUser.objects.filter(user__username=request.data["username"])
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PersonSerializer(data=request.data)
        data = request.data
        print(data)

        obj = PersonUser.objects.get(
            user__username = data["username"]
        )
        if data["system_dark_mode"] != None:
            obj.prefs_system_dark_mode = data["system_dark_mode"]
        
        if data["dark_mode"] != None:
            obj.prefs_dark_mode = data["dark_mode"]

        obj.save()

        # print(obj.points_given)
        # print(obj.result)

        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def answer_add(request):
    """
    List all code snippets, or create a new snippet.
    """
    print(request.data)

    if request.method == "GET":
        # memos = TestAnswers.objects.filter(curr_question=request)
        ta = TestAnswers.objects.all()
        serializer = QuestionAnswerSerializer(ta, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        test = Questionnaire.objects.get(id=request.data["test_practice"])
        cq = Question.objects.get(id=int(request.data["curr_question"]))

        test.answered_questions += 1
        test.save()
        
        test_answer, new_ta = TestAnswers.objects.get_or_create(
            curr_question = cq.id,
            question = cq,
            test_practice = test,
        )
        
        test_answer.options_ids = request.data["options_ids"]
        test_answer.known = request.data["known"]
        test_answer.points = cq.points

        answers =  request.data["options_ids"].split(',')

        answer = Option.objects.get(id=int(answers[0]))
        

        if request.data["postpone"] != True:
            test_answer.points_given = request.data["points"]
            if answer.correct:
                test_answer.result = 1
            else:
                test_answer.result = -1
        else:
            test_answer.postpone = True
            test_answer.result = 0
            test_answer.points_given = 0

        test_answer.save()

        return Response(new_ta, status=status.HTTP_201_CREATED)





@api_view(["POST"])
def flipp_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    # print(request.data)

    if request.method == "POST":
        cat_ids = []
        count = int(request.data["count"])
        cats = request.data["cats"]

        for c in cats:
            if c["use"]:
                cat_ids.append(int(c["id"]))

        # memos = TestAnswers.objects.filter(curr_question=request)
        flips = Question.objects.order_by("?").filter(category_id__in=cat_ids)[:count]
        serializer = QuestionSerializer(flips, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def practice_test(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == "GET":
        # memos = TestAnswers.objects.filter(curr_question=request)
        owner = PersonUser.objects.get(user__username=request.user)
        practice = Questionnaire.objects.filter(owner=owner).order_by("-created_date")[
            0:1
        ]
        serializer = QuestionnaireSerializer(practice, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        # serializer = QuestionnaireSerializer(data=request.data)
        data = request.data
        nuna = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M",
        )

        user = PersonUser.objects.get(user__username=data["user"])
        # print(user)
        # print(user.id)
        # print(data)

        obj = Questionnaire.objects.create(
            owner=user,
            timed=data["timed"],
            name=nuna,
            time_allowed=data["time_allowed"],
            omit_known=data["omit_known"],
            only_failed=data["only_failed"],
            question_collection_str=str(data["question_collection_str"]),
        )
        obj.save()

        i = 0  # index of array refers to Category id
        print(data["question_collection"])
        for q in data["question_collection"]:
            if q != None:
                print("actual q: ", q["id"])
                category = Category.objects.get(id=q["id"])
                # print(category.name)
                questions = category.question_set.all().order_by("?")
                # print(questions.count())
                quest_counter = 0
                for question in questions:
                    # print('quest_counter ', quest_counter)
                    if quest_counter < q["num"]:
                        if data["omit_known"] == False and data["only_failed"] == False:
                            # print("normal")
                            obj.question_collection.add(question)
                            quest_counter += 1
                        else:

                            known_flag = False

                            prev_answers = TestAnswers.objects.filter(
                                tesing_user=user,
                                curr_question=question.id,
                            )
                            # print(prev_answers)
                            """
                            If student wants to omit questions marked with -known- flag we have to test each optional 
                            question for the flag 
                            And if he only wants questions failed we also check
                            """

                            if len(prev_answers) > 0:
                                question_i = 0
                                question_results = 0
                                for a in prev_answers:
                                    if data["omit_known"] == True:
                                        if a.known == True:
                                            known_flag = True
                                            # break
                                    if data["only_failed"] == True:
                                        question_results += a.results
                                        question_i += 1
                                if question_results < 1 & known_flag == False:
                                    obj.question_collection.add(question)
                                    quest_counter += 1
                            else:
                                obj.question_collection.add(question)
                                quest_counter += 1

                                # obj.question_collection.add(question)
                                # quest_counter += 1

                            # if data['only_failed'] == True:
                            #     print('only_failed')
                            #     previous_results = TestAnswers.objects.filter(
                            #         user_id=user.id,
                            #         question=question.id,
                            #         result__gt=0
                            #     )
                            #
                            # if len(previous_results) == 0:
                            #     obj.question_collection.add(question)
                            #     quest_counter += 1

            i = i + 1
        obj.save()

        # if serializer.is_valid():
        #     serializer.save()
        return Response(status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def real_test(request):
    """
    List all code snippets, or create a new snippet.
    """

    print(request.method)

    if request.method == "GET":
        # memos = TestAnswers.objects.filter(curr_question=request)
        owner = PersonUser.objects.get(user__username=request.user)
        practice = Questionnaire.objects.filter(owner=owner).order_by("-created_date")[
            0:1
        ]
        serializer = QuestionnaireSerializer(practice, many=True)
        return Response(serializer.data)

    if request.method == "POST":

        total_questions = 60
        # serializer = QuestionnaireSerializer(data=request.data)
        data = request.data
        nuna = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M",
        )

        user = PersonUser.objects.get(user__username=data["user"])

        obj = Questionnaire.objects.create(
            owner=user,
            timed=data["timed"],
            name=nuna,
            time_allowed=data["time_allowed"],
            omit_known=False,
            only_failed=False,
            practice=False,
        )
        obj.save()

        categories = Category.objects.all()

        q_in_cat = int(total_questions / categories.count())

        for cat in categories:
            cat_quest = Question.objects.filter(category=cat).order_by("?")[0:q_in_cat]
            for q in cat_quest:
                print(q.category, q)
                obj.question_collection.add(q)

        print(obj)

        obj.save()
        serializer = QuestionnaireSerializer(obj, many=False)
        return Response(serializer.data)

        # if serializer.is_valid():
        #     serializer.save()
        # return Response(status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def practice_hand_in(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "POST":
        serializer = QuestionAnswerSerializer(data=request.data)
        data = request.data
        points = 0
        print('data')
        print(data)

        cq = Question.objects.get(id=int(data["curr_question"]))
        tp = Questionnaire.objects.get(id=int(data["test_practice"]))
        total_points = cq.points

        opt_answers = data["options_ids"].split(",")

        # print(opt_answers)

        if cq.single_selection:
            answered = Option.objects.filter(id=int(opt_answers[0]))
            if answered[0].correct:
                points = total_points
            # print(points)
        else:
            i = 0
            corrects = 0
            corr_opts = Option.objects.filter(
                id__in=cq.options, correct=True
            ).count()
            # print(corr_opts)

            points_per_correct = total_points / corr_opts

            anstring = data["options_ids"].split(",")
            tp.answered_questions = anstring.count()
            for answ in anstring:
                opt = Option.objects.get(id=int(answ))
                # print(opt.answer)
                # print(opt.correct)
                if opt.correct:
                    # print('correct')
                    corrects = corrects + points_per_correct
                    # print(corrects)
                else:
                    # print('wrong')
                    corrects = corrects - round(total_points / corr_opts)
                    # print(corrects)
                i += 1

            points = round(corrects)
            # points = round(corrects/total_points)
        # print(points)
        print('hérna')
        obj, newobj = TestAnswers.objects.get_or_create(
            # tesing_user=1,
            # time_allowed=data["time_allowed"],
            # time_taken=data["time_taken"],
            curr_question=cq.id,
            question=cq,
            options_ids=str(data["options_ids"]),
            test_practice=tp,
            points=points,
        )
        print('hérna líka')

        obj.save()

        return Response(newobj, status=status.HTTP_201_CREATED)

        # {'time_allowed': 120, 'time_taken': 46, 'options_ids': '149,150', 'curr_question': 49, 'test_practice': 48}

        # if serializer.is_valid():
        #     # serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
