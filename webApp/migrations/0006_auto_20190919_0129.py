# Generated by Django 2.2.5 on 2019-09-19 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0005_merge_20190919_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='project_fk',
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]