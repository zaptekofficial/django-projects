from django.db import models
from django.db.models import CharField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    datetime_created = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField('deadline')
    status = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
