from django.db import models


# Create your models here.
class CourseInfo(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20, default=None)
    dept = models.CharField(max_length=20, default=None)
    description = models.TextField(null=True, blank=True)
    prerequisites = models.TextField(null=True, blank=True)
    offered = models.CharField(max_length=100, null=True, blank=True)
    cross_listed = models.CharField(max_length=200, null=True, blank=True)
    credit_hours = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    @staticmethod
    def search_test(kw, dept_kw):
        kw = kw.upper()
        dept_kw = dept_kw.upper()
        global result
        # search in all departments
        if dept_kw == "ALL":
            print("searching in all depts")
            result1 = CourseInfo.objects.filter(course_code__iexact=kw).order_by('title')
            result2 = CourseInfo.objects.filter(title__icontains=kw).order_by('title')
            result3 = CourseInfo.objects.filter(description__icontains=kw).order_by('title')
            result = result1 | result2 | result3
            result.distinct()
        else:
            result1 = CourseInfo.objects.filter(dept=dept_kw).filter(course_code__iexact=kw).order_by('title')
            result2 = CourseInfo.objects.filter(dept=dept_kw).filter(title__icontains=kw).order_by('title')
            result3 = CourseInfo.objects.filter(dept=dept_kw).filter(description__icontains=kw).order_by('title')
            result = result1 | result2 | result3
            result.distinct()

        result = result.order_by('title')
        result_2 = list(result.values())
        return result_2


class ProfInfo(models.Model):
    url = models.URLField(blank=True, null=True, max_length=255)
    name = models.CharField(max_length=100)
    title = models.TextField(blank=True, null=True)
    dept = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    web_page = models.URLField(blank=True, null=True, max_length=255)
    focus = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True, max_length=255)

    # Update time
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    @staticmethod
    def search_test_prof(kw):
        kw = kw.upper()
        result_1 = ProfInfo.objects.filter(name__icontains=kw).order_by('name')
        result_2 = list(result_1.values())
        return result_2


class ProfAndCourses(models.Model):
    course_code = models.CharField(max_length=20, default="")
    dept = models.TextField(blank=True, null=True)
    code_digit = models.TextField(blank=True, null=True)
    prof = models.TextField(blank=True, null=True)
    section = models.TextField(blank=True, null=True)
    credit = models.TextField(blank=True, null=True)
    days = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    # Update time
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        get_latest_by = ['updated_at']
