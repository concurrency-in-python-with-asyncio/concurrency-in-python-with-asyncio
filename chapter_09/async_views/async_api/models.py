from django.db import models


class Url(models.Model):
    question_text = models.CharField(max_length=200)