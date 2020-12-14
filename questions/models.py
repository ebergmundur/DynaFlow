from django.db import models
from base.models import Base
from person.models import PersonUser
from django.utils.functional import cached_property
import pytz
from datetime import datetime
#from django.utils.translation import gettext as _

# Create your models here.

# default_user = PersonUser.objects.get(id=1)
default_user = 1

RESULT = [
    [-1, 'Failed'],
    [0, 'Postponed'],
    [1, 'Correct'],
]


class Category(Base):
    # group = models.ManyToManyField(Group, blank=True)
    # question = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "flokkur",
        verbose_name_plural = "flokkar"

    @property
    def q_count(self):
        return self.question_set.count
        # return QuestionGroupRelation.objects.filter(group=self.id).count()



class Question(Base):
    question = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
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
        if len(self.name) > 10:
            return self.name
        else:
            return self.question

    class Meta:
        verbose_name = "spurning",
        verbose_name_plural = "spurningar"
        ordering = ['?']

    @property
    def options(self):
        return self.question_option.all()

    @property
    def virtname(self):
        return self.__str__

    @property
    def answer_count(self):
        return self.options.count()

    @property
    def groups(self):
        return self.questiongrouprelation_set.all()

    @property
    def memos(self):
        return TestMemo.objects.filter(curr_question=self.id)
        # return TestMemo.objects.filter(curr_question=self.id, tesing_user=1 )


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
    checked = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s %s" % (self.name, self.answer, self.correct)

    class Meta:
        verbose_name = "svar",
        verbose_name_plural = "svör"
        ordering = ['?']

    @property
    def label(self):
        return self.answer

    @property
    def option(self):
        return self.answer\

    @property
    def value(self):
        return self.id\

    @property
    def selected(self):
        return self.checked


class Group(Base):
    owner = models.ForeignKey(PersonUser, on_delete=models.PROTECT, related_name="question_group_owner", related_query_name="group")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "hópur",
        verbose_name_plural = "hópar"

    # @property
    # def categories(self):
    #     return self.category_set.all()
    #
    # @property
    # def q_count(self):
    #     return self.questiongrouprelation_set.count
    #     # return QuestionGroupRelation.objects.filter(group=self.id).count()




class QuestionGroupRelation(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    order = models.SmallIntegerField(default=1)

    def __str__(self):
        return "%s - %s" % (self.question, self.group)

    class Meta:
        verbose_name = "tengd spurning",
        verbose_name_plural = "tengdar spurningar"


class Questionnaire(Base):
    owner = models.ForeignKey(PersonUser, default=1, on_delete=models.CASCADE, related_name="question_questionnaire_owner", related_query_name="questionnaire")
    timed = models.BooleanField(default=True, blank=True)
    time_allowed = models.SmallIntegerField(default=120, help_text="Mínútur", blank=True)
    question_collection = models.ManyToManyField(Question, blank=True)
    question_collection_str = models.CharField(max_length=200, blank=True)
    omit_known = models.BooleanField(default=False, blank=True)
    only_failed = models.BooleanField(default=False, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Próf/æfing",
        verbose_name_plural = "Próf/æfing"

    @property
    def q_count(self):
        return self.question_collection.count

    @property
    def answers(self):
        return self.testanswers_set.all()

    @property
    def results(self):
        optional_points = 0
        given_points = 0
        for a in self.testanswers_set.all():
            print(a)
            optional_points = optional_points + a.points
            given_points = given_points + a.points_given
        return {'optional_points': optional_points, 'given_points': given_points }


    @property
    def final_results(self):
        if self.results['optional_points'] > 0:
            return self.results['given_points'] / self.results['optional_points']
        else:
            return 0

# class QuestionnaireResults(models.Model):
#     user = models.ForeignKey(PersonUser, default=1, on_delete=models.PROTECT,)
#     questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT, )
#     question = models.ForeignKey(Question, on_delete=models.PROTECT)
#     result = models.SmallIntegerField(default=0, choices=RESULT)
#     result_date = models.DateTimeField(auto_now_add=True)


class QuestionnaireGroupRelation(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT)
    order = models.SmallIntegerField(default=1)

    def __str__(self):
        return "%s - %s" % (self.questionnaire, self.group)

    class Meta:
        verbose_name = "tengdur hópur",
        verbose_name_plural = "tengdir hópar"


class TestAnswers(Base):
    tesing_user = models.ManyToManyField(PersonUser, default=default_user, blank=True )
    curr_question = models.SmallIntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,  default=55)
    options_ids = models.CharField(max_length=200, default='')
    test_practice = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, default=1)
    points = models.SmallIntegerField(default=0)
    points_given = models.SmallIntegerField(default=0)
    known = models.BooleanField(default=False)
    postpone = models.BooleanField(default=False)
    result = models.SmallIntegerField(default=0, choices=RESULT)
    result_date = models.DateTimeField(auto_now_add=True)

    # @property
    # def question(self):
    #     return Question.objects.get(id=self.question_id)

    # def __str__(self):
    #     q = Question.objects.get(id=self.question_id)
    #     return '%s %s' % (self.user.get_full_name(), q.label)


class TestMemo(Base):
    tesing_user = models.ManyToManyField(PersonUser, blank=True, default=default_user)
    curr_question = models.SmallIntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=55)
    memo = models.TextField(blank=True)
    difficulty = models.SmallIntegerField(default=5)
    known = models.BooleanField(default=False)
    archive = models.BooleanField(default=True)
    review_date = models.DateField(blank=True, null=True)

    # @property
    # def question(self):
    #     return Question.objects.get(id=self.question_id)



def collect_questions(cats=[]):
    i = 0
    for q in cats:
        print(q)
        if q != None:
            try:
                category = Category.objects.get(id=i)
                print(category)
                questions = category.question.all()[:q]
                print(questions)
                for quest in questions:
                    # question_collection.add(quest)
                    pass
                # print(questions.count())
            except:
                pass
        i = i + 1