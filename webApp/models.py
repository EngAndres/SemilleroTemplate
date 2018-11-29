from django.db import models
from django.db import connection
from django.utils import timezone

# Create your models here.
######################## Project ########################
class Project(models.Model):
	id_project = models.IntegerField()
	name = models.TextField(unique = True)
	description = models.TextField(default = "")


######################## Member ########################
class Member(models.Model):
	id_member = models.IntegerField()
	name = models.TextField()
	nickname = models.TextField(unique = True)
	password = models.TextField()
	project_fk = models.ForeignKey(Project, on_delete = models.CASCADE)




######################## Semester ########################
class Semester(models.Model):
	id_semester = models.IntegerField()
	name = models.TextField()



######################## Candidate ########################

class Candidate(models.Model):
	name = models.TextField()
	email = models.TextField()
	subject = models.TextField()
	message = models.TextField()
	postulation_date = models.DateTimeField(default = timezone.now)
	semester_fk = models.ForeignKey(Semester, on_delete = models.CASCADE, default = None)





