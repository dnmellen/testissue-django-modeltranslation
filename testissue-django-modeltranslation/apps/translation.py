#See documentation in
#http://code.google.com/p/django-modeltranslation/wiki/InstallationAndUsage

from modeltranslation.translator import translator, TranslationOptions
from .models import Category


class CategoryTranslation(TranslationOptions):
    fields = ('name', )

translator.register(Category, CategoryTranslation)
