from modeltranslation.translator import register, TranslationOptions
from .models import Base
#from django.utils.translation import gettext as _

@register(Base)
class BaseTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
