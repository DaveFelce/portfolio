from __future__ import unicode_literals
from django.db import models

class Copy (models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.TextField(max_length=1000)
    intro = models.TextField(max_length=5000)
    text_column_1 = models.TextField(max_length=3000)
    text_column_2 = models.TextField(max_length=3000)
    text_column_3 = models.TextField(max_length=3000)

    class Meta:
        managed = True
        verbose_name_plural = "copy"


