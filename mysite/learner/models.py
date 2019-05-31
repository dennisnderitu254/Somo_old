from django.db import models


class Learner(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	learnerid = models.CharField(max_length=40)
	email = models.Charfield(max_length=50)

class Course(models.Model):
	courseid = models.CharField(max_length=50)
	coursename = models.CharField(max_length=50)