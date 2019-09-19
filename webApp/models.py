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
    cedula=models.integerField()
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

class Project(models.Model):
	name = models.CharField(max_length = 100, unique=True)
    description = models.CharField(max_length = 500, default='')
    image_path = models.CharField(max_length = 100, default='') 


class Rel_ProjectMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

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

class Archievement(models.Model): 
    name = models.CharField(max_length = 50, unique = True)
    description = models.CharField(max_length = 100, default = '')

class PublicationType(models.Model): 
    name = models.CharField(max_length = 40, unique = True)
    description = models.CharField(max_length = 100, default = '')

######################## Member ########################
""" class MemberManager(models.Manager):
	def create_member(self, id_, name_, nickname_, password_, project_):	#Similar to a constructor
		member = Member(id_member = id_, name = name_, nickname = nickname_, password = password_, project_fk = project_)
		return member

	def get_members(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM webApp_member;")
		members = cursor.fetchall()
		return members

	def get_member_by_id(self, id_):
		cursor = connection.cursor()
		cursor.execute("SELECT webApp_member.id AS id, webApp_member.name AS member, webApp_member.nickname AS nick, webApp_member.password AS psword, webApp_project.name AS project FROM webApp_member INNER JOIN webApp_project ON webApp_project.id = webApp_member.project_fk_id WHERE webApp_member.id_member = %s;", [id_])
		member = cursor.fetchall()
		return member

	def validate_login(self, nick_, psword_):
		cursor = connection.cursor()
		cursor.execute("SELECT COUNT(id)  FROM webApp_member WHERE nickname = %s AND password = %s;", [nick_, psword_])
		member = cursor.fetchone()
		return True if member == 1 else False 

	def insert_member(self, id_, name_, nick_, psword_, project_):
		cursor = connection.cursor()
		cursor.execute("INSERT INTO webApp_member(id_member, nickname, password, name, project_fk_id) VALUES (%s, %s, %s, %s, %s)", [id_, nick_, psword_, name_, project_])
		member = cursor.fetchone()
		return member

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
