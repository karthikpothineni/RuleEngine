from __future__ import unicode_literals

from django.db import models
from .base import BaseModel
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator


class Rules(BaseModel):
    rule_id = models.AutoField(primary_key=True, auto_created=True)
    rule_name = models.CharField(max_length=30)
    signal = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    value_type = models.CharField(max_length=30)
    criteria = models.CharField(max_length=30)

    class Meta:
        app_label = 'rule_engine'
        db_table = 'rules'

    def __str__(self):
        return str(self.rule_id)















