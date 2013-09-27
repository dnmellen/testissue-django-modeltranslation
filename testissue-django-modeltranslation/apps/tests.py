from django.test import TestCase
from django.utils.translation import trans_real
from .models import Category


class CategoryCreatedMixin(object):

    def setUp(self):
        # Here is the problematic code but works here!!
        Category.objects.create(name="Category one")


class BasicTest(CategoryCreatedMixin, TestCase):

    def test_create_category(self):

        # Retrieve category
        cat = Category.objects.get(name="Category one")
        self.assertEquals(cat.name, "Category one")

    def test_multiple_langs(self):

        category = Category.objects.get(name="Category one")

        trans_real.activate('en')
        category.name = "Category one english"
        category.save()
        trans_real.deactivate()
        trans_real.activate('es')
        category.name = "Categoria uno"
        category.save()
        trans_real.deactivate()

        # Retrieve category
        trans_real.activate('en')
        cat = Category.objects.all()[0]
        self.assertEquals(cat.name, "Category one english")
        trans_real.deactivate()

        trans_real.activate('es')
        cat = Category.objects.all()[0]
        self.assertEquals(cat.name, "Categoria uno")
        trans_real.deactivate()
