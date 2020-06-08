from django.shortcuts import render, redirect
from .models import MyUser, Title, Question, Solution, Teacher, Enrolled
from .forms import UserForm, MyUserForm, TitleForm, QuestionForm, SolutionForm, TeacherForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import  reverse_lazy
#Create your views here.

def login(request):

	if request.method == 'POST':


		val3 = request.POST['username']
		val4 = request.POST['password']

		user = auth.authenticate(username=val3, password=val4)

		if user is not None:
			auth.login(request, user)
			type = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
			if type == 'T':

				return redirect('users:create')

			else:
				return redirect('users:s_list')
		else:
			messages.error(request,'username or password not correct')
			return redirect('users:login')

	else:
		return render(request, 'login.html')


def register(request):
	form = UserForm
	my_form=MyUserForm
	if request.method == 'POST':
		# form = UserForm(request.POST or None)
		my_form = MyUserForm(request.POST or None)
		val1 = request.POST['first_name']
		val2 = request.POST['last_name']
		val3 = request.POST['username']
		val4 = request.POST['password']
		val5 = request.POST['confirm']
		if val4 == val5:
			if User.objects.filter(username=val3).exists():
				messages.error(request,'username aleady exist')
				return redirect('users:register')

			else:

				if my_form.is_valid():
			
				
					user = User.objects.create_user(username = val3, password = val4, first_name = val1, last_name = val2)
					user.save()
					profile = my_form.save(commit=False)
					profile.user=user
					profile.save()
	                
					type = my_form.cleaned_data.get('geeks_field')
					auth.login(request, user)
					if type == 'T':
						return redirect('users:teacher')
					elif type == 'S':
						return redirect('users:s_list')
					else:
						return redirect('users:register')


				else:
					return redirect('users:register')
		else:
			messages.error(request,'password not match')
			return redirect('users:register')

	        

	return render(request, 'register.html', {'form':form, 'my_form':my_form})



def logout(request):
    auth.logout(request)
    return redirect('/')



def home(request):

	if request.method == 'POST':


		val3 = request.POST['username']
		val4 = request.POST['password']

		user = auth.authenticate(username=val3, password=val4)

		if user is not None:
			auth.login(request, user)
			type = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
			if type == 'T':

				return redirect('users:create')

			else:
				return redirect('users:s_list')
		else:
			messages.error(request,'username or password not correct')
			return redirect('users:login')

	else:
		return render(request, 'home.html')










	
	# if not request.user.is_authenticated:
	# 	return render(request, 'home.html')
	# obj = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()

	
	# if obj == 'T':
	# 	return redirect('users:create')
	# elif obj == 'S':
	# 	return redirect('users:s_list')
	# else:
	# 	return redirect('users:register')


def create(request):
	if not request.user.is_authenticated:
		return redirect('users:login')

	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'T':

		code = Teacher.objects.filter(user=request.user).values_list('unique_code', flat=True).first()

		obj = Title.objects.all().filter(user=request.user)
		# return JsonResponse({'obj':obj})
		
		form = TitleForm

		if request.method == 'POST':

			form = TitleForm(request.POST or None)
			if form.is_valid():
				text = form.save(commit=False)
				text.user = request.user
				text.save()
				return redirect('users:question', id=text.id)

		else:
			return render(request, 'create.html', {'form':form, 'obj':obj, 'code':code})
	else:
		return redirect('users:s_list')



def question(request, id):
	if not request.user.is_authenticated:
		return redirect('users:logout')

	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'T':
		obj = Question.objects.all().filter(title_id=id)
		form = QuestionForm
		
		if request.method == 'POST':

			form = QuestionForm(request.POST or None)
			if form.is_valid():
				text = form.save(commit=False)
				text.title = Title.objects.filter(user=request.user).filter(id=id).first()
				text.save()
				
				return redirect('users:question', id=id)

		else:
			return render(request, 'question.html', {'form':form, 'obj':obj})

	else:
		return redirect('users:s_list')




def s_list(request):
	if not request.user.is_authenticated:
		return redirect('users:logout')
	obj = MyUser.objects.all().filter(geeks_field='T')
	oj = Enrolled.objects.all().filter(s_user=request.user)




	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'S':

		if request.method == 'POST':
			
			code = request.POST['code']
			j = Teacher.objects.filter(unique_code=code)

			c=Teacher.objects.filter(unique_code=code).values_list()
			

			if j.exists():
				
				l = Teacher.objects.get(unique_code=code)

				k=Enrolled.objects.filter(s_user=request.user).filter(code=l).values_list('code', flat=True)
				
				
				if len(k)>=1:
					return redirect('users:s_list')

				enroll=Enrolled.objects.create(user_id=c[0][1], s_user=request.user, code=l, name_to_display=c[0][2], subject=c[0][3])
				enroll.save()
				return redirect('users:s_list')
				


		return render(request, 's_list.html', {'obj':obj, 'oj':oj})
	else:
		return redirect('users:create')


def title_list(request, id):
	if not request.user.is_authenticated:
		return redirect('users:login')

	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'S':
	


		obj = Title.objects.all().filter(user=id)
		return render(request, 'title_list.html', {'obj':obj, 'val':id})

	else:
		return redirect('users:create')


def ques_list(request, id, val):
	if not request.user.is_authenticated:
		return redirect('users:login')

	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'S':
		x = request.user

		form = SolutionForm 
		obj = Question.objects.all().filter(title=id)
		obj1 = Solution.objects.filter(user=request.user).filter(title=id)

		if request.method=='POST':
			form = SolutionForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				text = form.save(commit=False)
				text.user = x
				text.title = Title.objects.filter(user=val).filter(id=id).first()
				
				text.save()

				return redirect('users:ques_list', id=id, val=val)


		return render(request, 'ques_list.html', {'obj':obj, 'obj1':obj1, 'form':form, 'value':val, 'pk':id})
	else:
		return redirect('users:create')


def delete(request, id, value, pk):
	if not request.user.is_authenticated:
		return redirect('users:login')

	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'S':

		x = Solution.objects.filter(id=id)
		x.delete()
		# x.save()
		return redirect('users:ques_list', pk, value)


	else:
		return redirect('users:create')



def teacher(request):

	if not request.user.is_authenticated:
		return redirect('users:login')
	
				
	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'T':
		x=Teacher.objects.filter(user=request.user).values_list('unique_code', flat=True).first()
		if x:
			return redirect('users:create')

		form = TeacherForm

		if request.method == 'POST':
			form = TeacherForm(request.POST or None)

			if form.is_valid():
				obj = form.save(commit=False)
				obj.user = request.user
				obj.save()


				return redirect('users:create')
			else:
				return redirect('users:teacher')
		return render(request, 'teacher.html', {'form':form})




	else:
		return redirect('users:s_list')



def join_list(request):

	if not request.user.is_authenticated:
		return redirect('users:login')

	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'S':
		return redirect('users:s_list')


	list = Enrolled.objects.all().filter(user=request.user)
	l = Enrolled.objects.filter(user=request.user).values_list('s_user_id', flat=True).first()

	return render(request, 'join_list.html', {'list':list})


def t_t_list(request, id):

	if not request.user.is_authenticated:
		return redirect('users:login')

	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'S':
		return redirect('users:s_list')



	obj = Title.objects.all().filter(user=request.user)
	return render(request, 't_t_list.html', {'obj':obj, 's_id':id})


def last(request, s_id, id):

	if not request.user.is_authenticated:
		return redirect('users:login')

	obj1 = MyUser.objects.filter(user=request.user).values_list('geeks_field', flat=True).first()
	
	if obj1 == 'S':
		return redirect('users:s_list')


	obj = Solution.objects.all().filter(user_id=s_id).filter(title=id)
	return render(request, 'last.html', {'obj':obj})

	