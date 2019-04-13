# Generated by Django 2.1.7 on 2019-03-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_delete_courseinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('course_code', models.CharField(default=None, max_length=20)),
                ('dept', models.CharField(default=None, max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('prerequisites', models.TextField(blank=True, null=True)),
                ('offered', models.CharField(blank=True, max_length=100, null=True)),
                ('cross_listed', models.CharField(blank=True, max_length=200, null=True)),
                ('credit_hours', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
