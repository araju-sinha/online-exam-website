from django.db import models

class Name(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    def __init__(self):
        return self.first_name

class Subject(models.Model):
    sub_text = models.CharField(max_length=30)

    def __init__(self):
        return self.sub_text

