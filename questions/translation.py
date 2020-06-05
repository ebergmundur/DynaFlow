from modeltranslation.translator import register, TranslationOptions
from .models import Question, Questionnaire, Option, Group, Category



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
