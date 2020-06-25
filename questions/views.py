from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OptionSerializer, QuestionSerializer
from .models import Option, Question,Questionnaire, QuestionGroupRelation, QuestionnaireGroupRelation, Group, Category


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer