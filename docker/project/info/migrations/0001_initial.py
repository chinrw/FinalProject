# Generated by Django 2.2 on 2019-04-13 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='ProfAndCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(default='', max_length=20)),
                ('dept', models.TextField(blank=True, null=True)),
                ('code_digit', models.TextField(blank=True, null=True)),
                ('prof', models.TextField(blank=True, null=True)),
                ('section', models.TextField(blank=True, null=True)),
                ('credit', models.TextField(blank=True, null=True)),
                ('days', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'get_latest_by': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ProfInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.TextField(blank=True, null=True)),
                ('dept', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('web_page', models.URLField(blank=True, max_length=255, null=True)),
                ('focus', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('image', models.URLField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
