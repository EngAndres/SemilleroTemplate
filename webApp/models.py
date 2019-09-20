from django.db import models
from django.db import connection
from django.utils import timezone

# Create your models here.
######################## Project ########################
class Area(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    description = models.CharField(max_length = 500, default='')
    
class Member(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    cedula=models.IntegerField()
    nickname = models.CharField(max_length = 20, unique=True)
    psword = models.CharField(max_length = 50, default='pass')
    email_unal = models.CharField(max_length = 50, unique=True)
    email_personal = models.CharField(max_length = 50, unique=True)
    cell_phone = models.CharField(max_length = 20, unique=True)
    link_CvLAC = models.CharField(max_length = 100, unique=True)
    #ubicacion=models.TextField() #TODO a futuro
    link_twitter = models.CharField(max_length = 100, unique=True)
    link_facebook = models.CharField(max_length = 100, unique=True)
    link_instagram = models.CharField(max_length = 100, unique=True)


class Archievement(models.Model): 
    name = models.CharField(max_length = 50, unique = True)
    description = models.CharField(max_length = 100, default = '')

######################## Member ########################
class ProjectManager(models.Manager):
	def create_project(self, id_, name_, description_, image_path_):	#Similar to a constructor
		project =Project(id_member = id_, name = name_,description =description_,image_path=image_path_)
		return project

	def get_project(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM webApp_project;")
		projects = cursor.fetchall()
		return projects

	def get_project_by_id(self, id_):
		cursor = connection.cursor()
		cursor.execute("SELECT webApp_project.id AS id, webApp_project.name AS name, webApp_project.description AS description, webApp_project.image_path AS image FROM webApp_project WHERE webApp_project.id = %s;", [id_])
		project = cursor.fetchall()
		return project

	def insert_project(self, name_, description_, image_path_):
		cursor = connection.cursor()
		cursor.execute("INSERT INTO webApp_project(name, description,image_path) VALUES (%s, %s, %s)", [name_, description_,image_path_])
		project= cursor.fetchone()
		return project

class Project(models.Model):
	name = models.CharField(max_length = 100, unique=True)
	description = models.CharField(max_length = 500, default='')
	image_path = models.CharField(max_length = 100, default='')
	project_ = ProjectManager()
 
class Rel_ProjectMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class PublicationType(models.Model): 
    name = models.CharField(max_length = 40, unique = True)
    description = models.CharField(max_length = 100, default = '')

class Publicaciones(models.Model):
    type_fk = models.ForeignKey(PublicationType, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100, default='')
    description = models.CharField(max_length = 500, default='')
    link= models.CharField(max_length = 100, default='')
    year = models.IntegerField(default='0000')
    
class Rel_PublicationProject(models.Model):
    publicacion=models.ForeignKey(Publicaciones, on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)

class Rel_ProductMembers(models.Model):
    member =models.ForeignKey(Member, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicaciones, on_delete=models.CASCADE)

"""
class Member(models.Model):
	id_member = models.IntegerField()
	name = models.TextField()
	nickname = models.TextField(unique = True)
	password = models.TextField()
	project_fk = models.ForeignKey(Project, on_delete = models.CASCADE)
	member_ = MemberManager()




######################## Semester ########################
class SemesterManager(models.Manager):
	def get_semesters(self):
		cursor = connection.cursor()
		cursor.execute("SELECT id_semester, name FROM webApp_semester;")
		semesters = cursor.fetchall()
		return semesters


class Semester(models.Model):
	id_semester = models.IntegerField()
	name = models.TextField()
	semester_ = SemesterManager()
	objects = models.Manager()



######################## Candidate ########################
class CandidateManager(models.Manager):
	def inser_candidate(self, name_, email_, subject_, message_, semester_):
		cursor = connection.cursor()
		cursor.execute("INSERT INTO webApp_candidate(name, email, subject, message, semester_fk) VALUES (%s, %s, %s, %s, %s)", [name_, email_, subject_, message_, semester_])
		member = cursor.fetchone()
		return member

class Candidate(models.Model):
	name = models.TextField()
	email = models.TextField()
	subject = models.TextField()
	message = models.TextField()
	postulation_date = models.DateTimeField(default = timezone.now)
	semester_fk = models.ForeignKey(Semester, on_delete = models.CASCADE, default = None)
	candidate_ = CandidateManager()

"""
