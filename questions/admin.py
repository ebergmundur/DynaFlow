from django.contrib import admin
from .models import Question, Option, Questionnaire, Category, Group, QuestionGroupRelation, QuestionnaireGroupRelation
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationGenericStackedInline, \
    TranslationStackedInline
import pytz
from datetime import datetime
from django.forms import ModelForm


@admin.register(Option)
class OptionAdmin(TabbedTranslationAdmin):

    def get_form(self, request, obj, **kwargs):
        form = super(OptionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['modified_by'].initial = request.user
        if form.base_fields['owner'].initial == None:
            form.base_fields['owner'].initial = request.user
        if form.base_fields['created_by'].initial == None:
            form.base_fields['created_by'].initial = request.user
        return form


class OptionInline(TranslationStackedInline):
    model = Option
    fk_name = 'question_ref'
    classes = ['collapse']
    # form = super(OptionAdmin, parent).get_form(request, obj, **kwargs)
    extra = 1


@admin.register(Question)
class QuestionAdmin(TabbedTranslationAdmin):
    inlines = [OptionInline, ]

    def get_form(self, request, obj, **kwargs):
        form = super(QuestionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['modified_by'].initial = request.user
        if form.base_fields['owner'].initial == None:
            form.base_fields['owner'].initial = request.user
        if form.base_fields['created_by'].initial == None:
            form.base_fields['created_by'].initial = request.user
        return form

    fieldsets = [
        (u'Spurning', {
            # 'classes': ('collapse','open' ),
            'fields': (
            'name',
            'points',
            'question',
            'image',
        )}),
        (u'Hint', {
            'classes': ('collapse', 'closed'),
            'fields': (
                'hint_cost',
                'hint',
            )}),
        (u'Ferill', {
            'classes': ('collapse', 'closed'),
            'fields': (
                'group_correct',
                'group_false',
            )}),
        (u'Lýsing, innispunktar og virkni', {
            'classes': ('collapse', 'closed'),
            'fields': (
                'description',
                'note',
                'active',
            )}),
        (u'Tími og stig', {
            'classes': ('collapse', 'closed'),
            'fields': (
                'timed',
                'time_allowed',
            )}),
        (u'Aðilar', {
            'classes': ('collapse', 'closed'),
            'fields': (
                'owner',
                'modified_by',
                'created_by',
            )}),
    ]


@admin.register(Group)
class GroupAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Questionnaire)
class QuestionnaireAdmin(TabbedTranslationAdmin):
    pass
