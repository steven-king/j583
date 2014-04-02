### https://docs.djangoproject.com/en/dev/topics/db/queries/


### to start django shell:
#python manage.py shell


### to import your models and data
from roster.models import Student, Course

### select all
students = Student.objects.all()

### select a single, specific student
student = Student.objects.get(pk=1)
course= Course.objects.get(callnumber="J187")

### select any item with a common data point using filter
fall2012Courses = Course.objects.filter(term="Fall 2012")
fall2012Courses = Course.objects.all.filter(term="Fall 2012") #same as above just shorter

###Querys build off of each other
fallCourses = fall2012Cources.filter(term__startswith="Fall")

##using exclude
nonAdvancedFallCources = fallCources.exclude(name__contains="Advanced")


## complex queries OR
easyCourses = Course.objects.filter(name__startswith='Intro') | Course.objects.filter(name__startswith='Intermediate')

## complex queries AND
hardCourses = Course.objects.exclude(name__startswith='Intro') & Course.objects.exclude(name__startswith='Intermediate')


## orderby
fall2012Courses = Course.objects.filter(term="Fall 2012").order_by('name')

## reverse! (order in opposit order)
fall2012Courses.reverse()
fall2012Courses.reverse()[:1] #last item in list


