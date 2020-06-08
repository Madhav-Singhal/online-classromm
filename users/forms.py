from django import forms
from .models import MyUser, Title, Question, Solution, Teacher
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    

    class Meta():

        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
    	user = super().save(commit=False)

    	
    	if commit:
    		user.save()
    	return user



class MyUserForm(forms.ModelForm):
	
	class Meta():
		model = MyUser
		fields = ('geeks_field',)



class TitleForm(forms.ModelForm):
    class Meta():
        model = Title
        fields = ('title',)



class QuestionForm(forms.ModelForm):

    class Meta():
        model = Question
        fields = ('ques',)



class SolutionForm(forms.ModelForm):

    class Meta():
        model = Solution
        fields = ('img',)


class TeacherForm(forms.ModelForm):

    class Meta():
        model = Teacher
        fields = ('name_to_display', 'subject', 'unique_code')