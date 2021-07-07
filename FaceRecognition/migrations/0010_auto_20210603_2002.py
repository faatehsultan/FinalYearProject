# Generated by Django 3.2.1 on 2021-06-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0009_auto_20210602_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=40)),
                ('section', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='sections',
        ),
    ]