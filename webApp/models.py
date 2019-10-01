from django.db import models
from django.db import connection
from django.utils import timezone

# Create your models here.
######################## Member ########################
class Area(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    description = models.CharField(max_length = 500, default='')

class MemberManager(models.Manager):
	def create_member(name_, cedula_, nickname_,psword_,email_unal_,email_personal_,cell_phone_,link_CvLAC_,link_twitter_,link_facebook_,link_instagram_):	#Similar to a constructor
		member =Member(name = name_,cedula =cedula_,nickname=nickname_,psword=psword_,email_unal=email_unal_,email_personal=email_personal_,cell_phone=cell_phone_,link_CvLAC=link_CvLAC_,link_twitter=link_twitter_,link_facebook=link_facebook_,link_instagram=link_instagram_)
		return member

	def get_member(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM webApp_member;")
		members = cursor.fetchall()
		return members

	def get_member_by_id(self, id_):
		cursor = connection.cursor()
		cursor.execute("SELECT webApp_member.id AS id, webApp_member.name AS name, webApp_member.cedula as cedula, webApp_member.nickname AS nickname, webApp_member.password AS password , webApp_member.email_unal AS unal, webApp_member.email_personal AS personal , webApp_member.cell_phone AS cell_phone , webApp_member.link_CvLAC AS link_CvLAC, webApp_member.link_twitter AS twitter , webApp_member.link_facebook AS facebook , webApp_member.link_instagram AS instagram  FROM webApp_member WHERE webApp_member.id = %s;", [id_])
		member = cursor.fetchall()
		return member

	def insert_member(self,name_, cedula_, nickname_,psword_,email_unal_,email_personal_,cell_phone_,link_CvLAC_,link_twitter_,link_facebook_,link_instagram_):
		cursor = connection.cursor()
		cursor.execute("INSERT INTO webApp_member(name, cedula,nickname,psword,email_unal,email_personal,cell_phone,link_CvLAC,link_twitter,link_facebook, link_instagram) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [name_, cedula_, nickname_,psword_,email_unal_,email_personal_,cell_phone_,link_CvLAC_,link_twitter_,link_facebook_,link_instagram_])
		member= cursor.fetchone()
		return member


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
	
class PublicationManager(models.Manager):
	def create_publication(self, id_, name_, description_,link_, year_):	#Similar to a constructor
		publication=Publication(id_member = id_, name = name_,description =description_,link=link_,year=year_)
		return publication

	def get_publication(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM webApp_publication;")
		publications = cursor.fetchall()
		return publications

	def get_publication_by_id(self, id_):
		cursor = connection.cursor()
		cursor.execute("SELECT webApp_publication.id AS id, webApp_publication.name AS name, webApp_publication.description AS description, webApp_publication.link AS link, webApp_publication.year AS year FROM webApp_publication WHERE webApp_publication.id = %s;", [id_])
		publications = cursor.fetchall()
		return publications

	def insert_publication(self, name_, description_,link_, year_):
		cursor = connection.cursor()
		cursor.execute("INSERT INTO webApp_publication(name, description,link,year) VALUES (%s, %s, %s,%s)", [ name_, description_,link_, year_])
		publication= cursor.fetchone()
		return publication


class Publication(models.Model):
    type_fk = models.ForeignKey(PublicationType, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100, default='')
    description = models.CharField(max_length = 500, default='')
    link= models.CharField(max_length = 100, default='')
    year = models.IntegerField(default='0000')
    
class Rel_PublicationProject(models.Model):
    publicacion=models.ForeignKey(Publication, on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)

class Rel_ProductMembers(models.Model):
    member =models.ForeignKey(Member, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publication, on_delete=models.CASCADE)

