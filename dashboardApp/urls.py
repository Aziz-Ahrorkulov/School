from django.urls import path
from . import views
urlpatterns = [
    path('Home-admin/', views.index, name= 'index'),
    path('Teachers/all-teachers/', views.all_teacher, name='all-teachers'),
    path('Teachers/add-teacher/', views.add_teacher, name='add-teacher'),
    path('edit-teacher/', views.edit_teacher, name='edit-teacher'),
    path('editdetail-teacher/', views.editTeacher_detailpage, name='editdetail-teacher'),
    path('about-teacher/', views.about_teacher, name='about-teacher'),
    path('aboutdetail-teacher/', views.aboutdetail_teacher, name='aboutdetail-teacher'),
    path('all-students/', views.all_students, name='all-students'),
    path('add-student/', views.add_student, name='add-student'),
    path('attendance/', views.attendance, name='attendance'),
    path('news-dashboard/', views.news_dashboard, name='news-dashboard'),
    path('messages/', views.direct_messages, name='messages'),
    path('user-profile/', views.profile_dashboard, name='profile-dashboard'),
    path('help/', views.help, name='help'),
]