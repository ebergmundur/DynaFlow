from modeltranslation.translator import register, TranslationOptions
from .models import Question, Questionnaire, Option, Group



@register(Question)
class BaseTranslationOptions(TranslationOptions):
    fields = ('question', 'hint',)

@register(Option)
class BaseTranslationOptions(TranslationOptions):
    fields = ('answer', )

# @register(Questionnaire)
# class BaseTranslationOptions(TranslationOptions):
#     fields = ('name', 'description',)
#
# @register(Group)
# class BaseTranslationOptions(TranslationOptions):
#     fields = ('name', 'description',)
