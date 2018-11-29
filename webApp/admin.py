from django.contrib import admin
from .models import Member
from .models import Project
from .models import Semester

# Register your models here.
admin.site.register(Member)
admin.site.register(Project)
admin.site.register(Semester)
