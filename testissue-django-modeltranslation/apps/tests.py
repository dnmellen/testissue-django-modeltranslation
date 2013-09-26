from django.test import TestCase
from django.utils.translation import trans_real
from .models import Category


class BasicTest(TestCase):

    def test_create_category(self):

        # Here is the problematic code!!
        Category.objects.create(name="Category one")
        # Retrieve category
        cat = Category.objects.get(name="Category one")
        self.assertEquals(cat.name, "Category one")

    def test_create_category_eng(self):

        # Here is the problematic code!!
        trans_real.activate('en')
        category = Category()
        category.name = "Category one"
        category.save()
        trans_real.deactivate()

        # Retrieve category
        cat = Category.objects.get(name="Category one")
        self.assertEquals(cat.name, "Category one")
        self.assertEquals(cat.name_en, "Category one")
