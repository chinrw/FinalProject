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
    def search_course_tool(kw, dept_kw, sort_option=1):
        kw = kw.upper()
        dept_kw = dept_kw.upper()
        global result
        # search in all departments
        if dept_kw == "ALL":
            print(sort_option)
            print("searching in all depts")
            result1 = CourseInfo.objects.filter(course_code__iexact=kw)
            result2 = CourseInfo.objects.filter(title__icontains=kw)
            result3 = CourseInfo.objects.filter(description__icontains=kw)
            result = result1 | result2 | result3
            result.distinct()
        else:
            result1 = CourseInfo.objects.filter(dept=dept_kw).filter(course_code__iexact=kw)
            result2 = CourseInfo.objects.filter(dept=dept_kw).filter(title__icontains=kw)
            result3 = CourseInfo.objects.filter(dept=dept_kw).filter(description__icontains=kw)
            result = result1 | result2 | result3
            result.distinct()
        if sort_option == "1":
            print("order1")
            result = result.order_by('title')
        elif sort_option == "2":
            print("order")
            result = result.order_by('course_code')
        # for x in range(0, len(result)):
        #     print(result[x].title)
        result_2 = list(result.values())
        # print(result_2)
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
    def search_prof_tool(kw):
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

    @staticmethod
    def search_course_by_prof(kw):
        # print(kw)
        result_1 = ProfAndCourses.objects.filter(prof__icontains=kw)
        result_2 = list(result_1.values("course_code"))
        # print(result_2)
        result_3 = []
        for x in result_2:
            if CourseInfo.objects.filter(course_code__icontains=x['course_code']).values():
                result_3.append(list(CourseInfo.objects.filter(course_code__icontains=x['course_code']).values())[0])
        # result_3 = list(result_3.values())
        # for x in result_3:
        #     print(x['title'])
        return result_3

    @staticmethod
    def search_prof_by_dept(dept, name):
        result_1 = ProfAndCourses.objects.filter(dept__iexact=dept).filter(prof__icontains=name)
        # list of professors in the specified dept found
        result_1 = list(result_1.values("prof"))
        result_2 = ProfInfo.search_prof_tool(name)
        result_3 = []
        for x in result_2:
            for y in result_1:
                if x["name"].lower() in y["prof"].lower():
                    result_3.append(x)
                    break
        # print(result_3)
        return result_3


class RelatedPages(models.Model):
    links = models.URLField(max_length=512)
    title = models.TextField(blank=True, null=True)
    course = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    # Update time
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
