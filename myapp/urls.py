from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('schools/', views.schools, name='school'),
    path('news/', views.news, name='news'),
    path('course/', views.course, name='course'),
    path('course-datails/<int:id>/', views.course_details, name= 'course-details'),
    path('about-us/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'), 
    path('logout/', views.logout_user, name='logout'), 
    path('register/', views.register, name='register'), 
    path('school-detail/<int:id>/', views.school_detail, name='school-detail'), 
    path('new-detail/<int:id>/', views.new_detail, name='new-detail'), 
    path('profile/<int:id>/', views.profile, name='profile'), 
    path('update-user/', views.update_user, name='update-user'), 
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)