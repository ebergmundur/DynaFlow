from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OptionSerializer, QuestionSerializer, QuestionMemoSerializer
from .models import Option, Question,Questionnaire, QuestionGroupRelation, QuestionnaireGroupRelation, Group, Category


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class QuestionMemoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    memo = Option.objects.all()
    serializer_class = QuestionMemoSerializer