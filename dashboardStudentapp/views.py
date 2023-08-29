from django.shortcuts import render

# Create your views here.


def home_student(request):
    return render(request, 'dashboard-student-pages/index-students.html')

def dairy_student(request):
    return render(request, 'dashboard-student-pages/dairy-students.html')
    
def homework_student(request):
    return render(request, 'dashboard-student-pages/homework-students.html')

def allclassmates_student(request):
    return render(request, 'dashboard-student-pages/all-classmates.html')

def all_students(request):
    return render(request, 'dashboard-student-pages/all-students-school.html')

def school_staff(request):
    return render(request, 'dashboard-student-pages/school-staff.html')

def course(request):
    return render(request, 'dashboard-student-pages/course-studdent.html')

def news_ownschool(request):
    return render(request, 'dashboard-student-pages/news-ownschool.html')

def news_otherschool(request):
    return render(request, 'dashboard-student-pages/news-otherschool.html')

def student_profile(request):
    return render(request, 'dashboard-student-pages/student-profile.html')

def users_profile(request):
    return render(request, 'dashboard-student-pages/users-profile.html')