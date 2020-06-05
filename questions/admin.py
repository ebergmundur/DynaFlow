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
class OptionAdmin(TranslationAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    pass



