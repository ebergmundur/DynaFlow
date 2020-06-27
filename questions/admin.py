from django.contrib import admin
from .models import Question, Option, Questionnaire, Category, Group, QuestionGroupRelation, QuestionnaireGroupRelation
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationGenericStackedInline, \
    TranslationStackedInline
import pytz
from datetime import datetime
from django.forms import ModelForm
from functools import partial


def curry(func, *a, **kw):
    return partial(func, *a, **kw)


@admin.register(Option)
# class OptionAdmin(admin.ModelAdmin):
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
    extra = 1

    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        formset = super(OptionInline, self).get_formset(request, obj, **kwargs)
        formset.form.base_fields['modified_by'].initial = request.user
        if formset.form.base_fields['owner'].initial == None:
            formset.form.base_fields['owner'].initial = request.user
        if formset.form.base_fields['created_by'].initial == None:
            formset.form.base_fields['created_by'].initial = request.user
        return formset

    fieldsets = [
        (u'Svar', {
            'classes': ('collapse',),
            'fields': (
                'answer',
                'correct',
                'image',
            )}),
        (u'Gildi', {
            'classes': ('collapse', 'closed'),
            'fields': (
                'value_from',
                'correct_value_from',
                'value_to',
                'correct_value_to',
            )}),
        (u'Lýsing, innispunktar og virkni', {
            'classes': ('collapse', 'closed'),
            'fields': (
                'description',
                'note',
                'active',
            )}),
        (u'Aðilar', {
            'classes': ('collapse', 'closed'),
            'fields': (
                'owner',
                'modified_by',
                'created_by',
            )}),
    ]


@admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
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

    # def get_formsets_with_inlines(self, request, obj=None):
    #     for inline in self.get_inline_instances(request, obj):
    #         inlformset = inline.get_formset(request, obj)
    #         # hide/show market-specific inlines based on market name
    #         # optform = super(OptionInline, inline).get_formset(request, obj)
    #         x = 1
    #         yield inline.get_formset(request, obj), inline

    fieldsets = [
        (u'Spurning', {
            'classes': ('collapse', 'open'),
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
