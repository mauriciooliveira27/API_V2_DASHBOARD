from django.db import models
from datetime import datetime
from django.utils import timezone

class Base(models.Model):

    create = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)
    class Meta:
        abstract = True


class DashBoard(Base):
    
    balanca = models.JSONField(null=True)

