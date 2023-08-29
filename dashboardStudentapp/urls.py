from django.urls import path
from . import views

urlpatterns = [
    path('Home-student/', views.home_student, name ='home-student'),
    path('Образование/Dairy-student/', views.dairy_student, name ='dairy-students'),
    path('Образование/Homework-student/', views.homework_student, name ='homework-students'),
    path('Моя-Школа/all-classmates/', views.allclassmates_student, name ='allclassmates-students'),
    path('Моя-Школа/all-students/', views.all_students, name ='all-students'),
    path('Моя-Школа/school-staff/', views.school_staff, name ='school-staff'),
    path('Home-student/Курсы/', views.course, name ='course-student'),
    path('Новости/Новости-про-вашу-школу/', views.news_ownschool, name ='news-ownschool'),
    path('Новости/Новости-про-доругих-школ/', views.news_otherschool, name ='news-otherschool'),
    path('Profile', views.student_profile, name ='student-profile'),
    path('User/qeqwsq34as23', views.users_profile, name ='users-profile'),
]