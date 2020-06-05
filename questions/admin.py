from django.contrib import admin
from .models import Question, Option, Questionnaire, Category, Group, QuestionGroupRelation, QuestionnaireGroupRelation
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationGenericStackedInline, \
    TranslationStackedInline


class OptionInline(TranslationStackedInline):
    model = Option
    fk_name = 'question_ref'
    classes = ['collapse']
    extra = 1

@admin.register(Question)
class QuestionAdmin(TabbedTranslationAdmin):
    inlines = [OptionInline,]
    pass

    # fieldsets = [
    #     (u'Question', {'fields': (
    #         #'name',
    #         #'description'
    #         'question',
    #         'hint',
    #     )})
    # ]



@admin.register(Option)
class OptionAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Group)
class GroupAdmin(TabbedTranslationAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Questionnaire)
class QuestionnaireAdmin(TabbedTranslationAdmin):
    pass



