from django.contrib import admin
from .models import Question, Option, Questionnaire, Category, Group, QuestionGroupRelation, QuestionnaireGroupRelation, \
    TestMemo, TestAnswers, QuestionsAndAnswers, TextBlock
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationGenericStackedInline, \
    TranslationStackedInline, TranslationInlineModelAdmin, TranslationTabularInline
import pytz
from datetime import datetime
from django.forms import ModelForm
from functools import partial


def curry(func, *a, **kw):
    return partial(func, *a, **kw)


@admin.register(Option)
class OptionAdmin(TabbedTranslationAdmin):
    list_display = ('answer', 'question_ref', 'name', 'correct', 'owner')
    list_filter = ['question_ref__name', 'owner__user__username', 'correct', ]

    def get_form(self, request, obj, **kwargs):
        form = super(OptionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['modified_by'].initial = request.user
        if form.base_fields['owner'].initial == None:
            form.base_fields['owner'].initial = request.user
        if form.base_fields['created_by'].initial == None:
            form.base_fields['created_by'].initial = request.user
        return form

    #     fieldsets = [
    #         (u'Svar', {
    #             'classes': ('collapse', 'open',),
    #             'fields': (
    #                 'answer',
    #                 'correct',
    #                 'image',
    #                 'active',
    #             )}),
    #         (u'Gildi', {
    #             'classes': ('collapse', 'collapsed'),
    #             'fields': (
    #                 'value_from',
    #                 'correct_value_from',
    #                 'value_to',
    #                 'correct_value_to',
    #             )}),
    #         (u'Lýsing, innispunktar og virkni', {
    #             'classes': ('collapse', 'collapsed',),
    #             'fields': (
    #                 'description',
    #                 'note',
    #             )}),
    #         (u'Aðilar', {
    #             'classes': ('collapse', 'collapsed'),
    #             'fields': (
    #                 'owner',
    #                 'modified_by',
    #                 'created_by',
    #             )}),
    # ]

    fieldsets = [
        (u'Spurning', {
            'fields': (
                'answer',
                'correct',
                'image',
                'active',
            ),
            'classes': (
                'baton-tabs-init', 'baton-tab-fs-optvalue', 'baton-tab-fs-optnote',
                'baton-tab-fs-optowner',),
            'description': 'This is a description text',
        }),
        (u'Gildi', {
            'classes': ('tab-fs-optvalue',),
            'fields': (
                'value_from',
                'correct_value_from',
                'value_to',
                'correct_value_to',
            )}),
        (u'Lýsing, innispunktar og virkni', {
            'fields': (
                'description',
                'note',
            ),
            'classes': ('tab-fs-optnote',),
        }),
        (u'Aðilar', {
            'fields': (
                'owner',
                'modified_by',
                'created_by',
            ),
            'classes': ('tab-fs-optowner',),
        }),
    ]


class OptionInline(TranslationTabularInline):
    model = Option
    fk_name = 'question_ref'
    extra = 1

    # classes = ('collapse-entry',)
    # classes = ( 'collapse-entry','collapse',  )
    # classes = ('collapse',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(OptionInline, self).get_formset(request, obj, **kwargs)
        formset.form.base_fields['modified_by'].initial = request.user
        if formset.form.base_fields['owner'].initial == None:
            formset.form.base_fields['owner'].initial = request.user
        if formset.form.base_fields['created_by'].initial == None:
            formset.form.base_fields['created_by'].initial = request.user
        return formset

    #     fieldsets = [
    #         (u'Svar', {
    #             'classes': ( 'collapse', 'collapsed', ),
    #             'fields': (
    #                 'name',
    #                 'answer',
    #                 'correct',
    #                 'image',
    #                 'active',
    #             )}),
    #         (u'Gildi', {
    #             'classes': ( 'collapse', 'collapsed', ),
    #             'fields': (
    #                 'value_from',
    #                 'correct_value_from',
    #                 'value_to',
    #                 'correct_value_to',
    #             )}),
    #         (u'Lýsing, innispunktar og virkni', {
    #             'classes': ( 'collapse', 'collapsed', ),
    #             'fields': (
    #                 'description',
    #                 'note',
    #             )}),
    #         (u'Aðilar', {
    #             'classes': ( 'collapse', 'collapsed', ),
    #             'fields': (
    #                 'owner',
    #                 'modified_by',
    #                 'created_by',
    #             )}),
    # ]

    fieldsets = [
        (u'', {
            'fields': (
                # 'name',
                'answer',
                'correct',
                'image',
                'active',
            ),
            'classes': (),
            # 'classes': (
            #    'baton-tab-fs-optvalue', 'baton-tab-fs-optnote',
            #     'baton-tab-fs-optowner',),
            # 'description': 'This is a description text',
        }),
        # (u'Gildi', {
        #     'fields': (
        #         'value_from',
        #         'correct_value_from',
        #         'value_to',
        #         'correct_value_to',
        #     ),
        #     'classes': ('collapse', 'collapsed',),
        #     # 'classes': ('tab-fs-optvalue',),
        # }),
        # (u'Lýsing, innispunktar og virkni', {
        #     'fields': (
        #         'description',
        #         'note',
        #     ),
        #     'classes': ('collapse', 'collapsed',),
        #     # 'classes': ('tab-fs-optnote',),
        # }),
        (u'Aðilar', {
            # TODO prófa að fela
            'fields': (
                'owner',
                'modified_by',
                'created_by',
            ),
            'classes': ('collapse', 'collapsed',),
            # 'classes': ('tab-fs-otpowner',),
        }),
    ]


@admin.register(Question)
class QuestionAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'question', 'category', 'exam_question', 'flipcard_question', 'answer_count', 'owner','single_selection',)
    inlines = [OptionInline, ]
    list_filter = [ 'category', 'owner', 'exam_question', 'single_selection',]
    list_editable = ['single_selection', 'exam_question', 'category', 'flipcard_question', ]

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
            'fields': (
                'name',
                'exam_question',
                'single_selection',
                'points',
                'question',
                'category',
                'hint_cost',
                'hint',
                'image',
                'active',
            ),
            'classes': (
                'baton-tabs-init',
                # 'baton-tab-fs-hint',
                # 'baton-tab-fs-ferill',
                # 'baton-tab-fs-note',
                # 'baton-tab-fs-time',
                'baton-tab-fs-owner',
                'baton-tab-inline-question_option',
            ),
            'description': 'This is a description text',
        }),
        # (u'Hint', {
        #     'classes': ('tab-fs-hint',),
        #     'fields': (
        #         'hint_cost',
        #         'hint',
        #     )}),
        # (u'Ferill', {
        #     'fields': (
        #         'group_correct',
        #         'group_false',
        #     ),
        #     'classes': ('tab-fs-ferill',),
        # }),
        # (u'Lýsing, innispunktar og virkni', {
        #     'fields': (
        #         'description',
        #         'note',
        #     ),
        #     'classes': ('tab-fs-note',),
        # }),
        # (u'Tími og stig', {
        #     'fields': (
        #         'timed',
        #         'time_allowed',
        #     ),
        #     'classes': ('tab-fs-time',),
        # }),
        (u'Aðilar', {
            'fields': (
                'owner',
                'modified_by',
                'created_by',
            ),
            'classes': ('tab-fs-owner',),
        }),
    ]


@admin.register(Group)
class GroupAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'order')
    list_editable = ['order']


@admin.register(Questionnaire)
class QuestionnaireAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'practice', 'owner', 'q_count', 'results' )
    filter_horizontal = ['question_collection']
    list_editable = ['practice']


# @admin.register(QuestionGroupRelation)
# class QuestionGroupRelationAdmin(admin.ModelAdmin):
#     pass


@admin.register(TestMemo)
class TestMemoAdmin(TabbedTranslationAdmin):
    pass

@admin.register(QuestionsAndAnswers)
class QuestionsAndAnswersAdmin(TabbedTranslationAdmin):
    pass

@admin.register(TextBlock)
class QuestionsAndAnswersAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'spot', 'order', )
    list_filter = ['spot']
    list_editable = ['order']
    fieldsets = [
        (u'', {
            'fields': (
                'name',
                'spot',
                'order',
                # 'slot',
                'description',
            ),
            'classes': (),
        }),
        (u'Aðilar', {
            # TODO prófa að fela
            'fields': (
                # 'owner',
                'modified_by',
                'created_by',
            ),
            'classes': ('collapse', 'collapsed',),
            # 'classes': ('tab-fs-otpowner',),
        }),
    ]

@admin.register(TestAnswers)
class TestAnswersAdmin(TabbedTranslationAdmin):
    list_display = ('result_date', 'result', 'test_practice', 'tesing_user', 'known', 'postpone', 'question_category_name', 'question', 'points_given' )
    list_filter = [ 'test_practice', 'tesing_user', 'points_given' ]
    list_editable = ['points_given' ]
