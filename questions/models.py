from django.db import models
from base.models import Base
from person.models import PersonUser
#from django.utils.translation import gettext as _

# Create your models here.

class Question(Base):
    question = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)
    owner = models.ForeignKey(PersonUser, on_delete=models.PROTECT, related_name="question_question_owner", related_query_name="question_owner")
    timed = models.BooleanField(default=False)
    time_allowed = models.SmallIntegerField(default=120, help_text="Sekúndur")
    single_selection = models.BooleanField(default=False)
    points = models.SmallIntegerField(default=5)
    hint = models.TextField(blank=True)
    hint_cost = models.SmallIntegerField(default=3)
    group_correct = models.ForeignKey("Group", blank=True, null=True, related_name="group_correct", on_delete=models.PROTECT )
    group_false = models.ForeignKey("Group", blank=True, null=True, related_name="group_false", on_delete=models.PROTECT )

    @property
    def options(self):
        return self.question_option.all()


class Option(Base):
    question_ref = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_option", related_query_name="question_option_option")
    owner = models.ForeignKey(PersonUser, on_delete=models.PROTECT, related_name="question_option_owner", related_query_name="option_owner")
    answer = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)
    value_from = models.FloatField(default=0.0)
    value_to = models.FloatField(default=0.0)
    correct_value_from = models.FloatField(default=0.0)
    correct_value_to = models.FloatField(default=0.0)
    image = models.ImageField(blank=True)




class Group(Base):
    owner = models.ForeignKey(PersonUser, on_delete=models.PROTECT, related_name="question_group_owner", related_query_name="group")

class Category(Base):
    group = models.ManyToManyField(Group, blank=True)


class QuestionGroupRelation(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    order = models.SmallIntegerField(default=1)


class Questionnaire(Base):
    owner = models.ForeignKey(PersonUser, on_delete=models.PROTECT, related_name="question_questionnaire_owner", related_query_name="questionnaire")
    timed = models.BooleanField(default=False)
    time_allowed = models.SmallIntegerField(default=120, help_text="Mínútur")


class QuestionnaireGroupRelation(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT)
    order = models.SmallIntegerField(default=1)