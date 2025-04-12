from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth  import get_user_model
# from django.contrib.gis.db import models as gis_models

# Create your models here.


class Issue(models.Model):
    description = models.CharField(max_length=500)
    creater = get_user_model()
    time = models.DateField(auto_now_add=True)
    # location = gis_models.PointField(srid=4326)

    class Meta:
        verbose_name = 'Issues'


class LocalLegislation(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True)
    legislation = models.CharField(max_length=500)
    time = models.DateField(auto_now_add=True)


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    responce = models.CharField(max_length=100, null=True)

class Question(models.Model):
    question = models.CharField(max_length=200)
    option = models.ForeignKey('Option', on_delete=models.CASCADE)

class Option(models.Model):
    description = models.CharField(max_length=100)


class Poll(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)


