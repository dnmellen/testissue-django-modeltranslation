
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=75)

    def __unicode__(self):
        return u'Category {}'.format(self.name)
