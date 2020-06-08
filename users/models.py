from django.db import models
from django.contrib.auth.models import User

CHOICES =( 
    ("T", "teacher"),
    ("S", "student")
) 
class MyUser(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	geeks_field = models.CharField(max_length=7, choices = CHOICES)
    

	def __str__(self):
		return self.user.username


class Title(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	title = models.CharField(max_length=100)
	

	def __str__(self):
		return self.title


class Teacher(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name_to_display = models.CharField(max_length=50)
	subject = models.CharField(max_length=100)
	unique_code = models.CharField(max_length=10, unique = True)


	def __str__(self):
		return self.unique_code


class Enrolled(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teach')
	s_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
	code = models.ForeignKey(Teacher, on_delete=models.CASCADE)

	name_to_display = models.CharField(max_length=50)
	subject = models.CharField(max_length=100)


	def __str__(self):
		return self.name_to_display





class Question(models.Model):
	title = models.ForeignKey(Title, on_delete=models.CASCADE)
	ques = models.TextField()

	def __str__(self):
		return self.ques



class Solution(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	title = models.ForeignKey(Title, on_delete=models.CASCADE)
	img = models.FileField(upload_to = 'pics/', blank=True, null=True)

	def __str__(self):
		return self.user.username    




