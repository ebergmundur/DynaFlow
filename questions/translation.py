from modeltranslation.translator import register, TranslationOptions
from .models import Question, Questionnaire, Option, Group, Category, TestAnswers, TestMemo, QuestionGroupRelation, \
    QuestionnaireGroupRelation, QuestionsAndAnswers



@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'hint',)

@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('answer', )

@register(Questionnaire)
class QuestionnaireTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)



@register(TestMemo)
class TestMemoTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)



@register(TestAnswers)
class TestAnswersTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(QuestionsAndAnswers)
class TestAnswersTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)




# @register(QuestionGroupRelation)
# class QuestionGroupRelationTranslationOptions(TranslationOptions):
#     fields = ('name', 'description',)
#
#
#
#
# @register(QuestionnaireGroupRelation)
# class QuestionnaireGroupRelationTranslationOptions(TranslationOptions):
#     fields = ('name', 'description',)
#

