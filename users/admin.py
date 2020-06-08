from django.contrib import admin

from .models import MyUser, Title, Question, Solution, Teacher, Enrolled

admin.site.register(MyUser)
admin.site.register(Title)
admin.site.register(Question)
admin.site.register(Solution)
admin.site.register(Teacher)
admin.site.register(Enrolled)


