from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
		path('', views.home, name='home'),
		path('login/', views.login, name='login'),
		path('register/', views.register, name='register'),
		path('logout/', views.logout, name='logout'),
		path('create/', views.create, name='create'),
		path('s_list/', views.s_list, name='s_list'),
		path('<int:id>/question/', views.question, name='question'),

		
		path('create/join_list', views.join_list, name='join_list'),

		path('<int:id>/title_list', views.title_list, name='title_list'),
		path('<int:id>/<int:val>/ques_list', views.ques_list, name='ques_list'),
		path('<int:id>/<int:value>/<int:pk>/delete', views.delete, name='delete'),

		path('teacher/', views.teacher, name='teacher'),
		path('create/t_t_list/<int:id>', views.t_t_list, name='t_t_list'),
		path('create/<int:s_id>/<int:id>/last', views.last, name='last'),


]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

