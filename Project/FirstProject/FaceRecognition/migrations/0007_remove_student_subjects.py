# Generated by Django 3.2.1 on 2021-05-24 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0006_alter_student_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
    ]