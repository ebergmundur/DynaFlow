from django.db import models
from base.models import Base
from person.models import PersonUser
import pytz
from datetime import datetime
#from django.utils.translation import gettext as _

# Create your models here.

class Question(Base):
    question = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='questionImage')
    owner = models.ForeignKey(PersonUser, on_delete=models.PROTECT, related_name="question_question_owner", related_query_name="question_owner")
    timed = models.BooleanField(default=False)
    time_allowed = models.SmallIntegerField(default=120, help_text="Sekúndur")
    single_selection = models.BooleanField(default=False)
    points = models.SmallIntegerField(default=5)
    hint = models.TextField(blank=True)
    hint_cost = models.SmallIntegerField(default=3)
    group_correct = models.ForeignKey("Group", blank=True, null=True, related_name="group_correct", on_delete=models.PROTECT )
    group_false = models.ForeignKey("Group", blank=True, null=True, related_name="group_false", on_delete=models.PROTECT )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "spurning",
        verbose_name_plural = "spurningar"

    @property
    def options(self):
        return self.question_option.all()

    @property
    def answer_count(self):
        return self.options.count()

    @property
    def groups(self):
        return self.questiongrouprelation_set.all()


class Option(Base):
    question_ref = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_option", related_query_name="question_option_option")
    owner = models.ForeignKey(PersonUser, on_delete=models.PROTECT, related_name="question_option_owner", related_query_name="option_owner")
    answer = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)
    value_from = models.FloatField(default=0.0)
    value_to = models.FloatField(default=0.0)
    correct_value_from = models.FloatField(default=0.0)
    correct_value_to = models.FloatField(default=0.0)
    image = models.ImageField(blank=True, upload_to='optionImage' )

    def __str__(self):
        return "%s %s %s" % (self.name, self.answer, self.correct)

    class Meta:
        verbose_name = "svar",
        verbose_name_plural = "svör"


class Group(Base):
    owner = models.ForeignKey(PersonUser, on_delete=models.PROTECT, related_name="question_group_owner", related_query_name="group")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "hópur",
        verbose_name_plural = "hópar"

class Category(Base):
    group = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "flokkur",
        verbose_name_plural = "flokkar"


class QuestionGroupRelation(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    order = models.SmallIntegerField(default=1)

    def __str__(self):
        return "%s - %s" % (self.question, self.group)

    class Meta:
        verbose_name = "tengd spurnin",
        verbose_name_plural = "tengdar spurningar"


class Questionnaire(Base):
    owner = models.ForeignKey(PersonUser, on_delete=models.PROTECT, related_name="question_questionnaire_owner", related_query_name="questionnaire")
    timed = models.BooleanField(default=False)
    time_allowed = models.SmallIntegerField(default=120, help_text="Mínútur")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "spurningalisti",
        verbose_name_plural = "spurningalistar"


class QuestionnaireGroupRelation(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT)
    order = models.SmallIntegerField(default=1)

    def __str__(self):
        return "%s - %s" % (self.questionnaire, self.group)

    class Meta:
        verbose_name = "tengdur hópur",
        verbose_name_plural = "tengdir hópar"