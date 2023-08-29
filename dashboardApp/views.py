from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dashboard-admin-pages/index-admin.html')


# ==== Admin ==== 

# TEACHERS

def all_teacher(request):
    return render(request, 'dashboard-admin-pages/all-teachers.html')

def add_teacher(request):
    return render(request, 'dashboard-admin-pages/add-teacher.html')

def edit_teacher(request):
    return render(request, 'dashboard-admin-pages/edit-teacher.html')

def editTeacher_detailpage(request):
    return render(request, 'dashboard-admin-pages/edit-teacher-detail.html')

def about_teacher(request):
    return render(request, 'dashboard-admin-pages/about-teacher.html')

def aboutdetail_teacher(request):
    return render(request, 'dashboard-admin-pages/aboutdetail-teacher.html')


# STUDENTS 

def all_students(request):
    return render(request, 'dashboard-admin-pages/all-students.html')


def add_student(request):
    return render(request, 'dashboard-admin-pages/add-student.html')


# ATTENDANCE

def attendance(request):
    return render(request, 'dashboard-admin-pages/attendance.html')

# NEWS

def news_dashboard(request):
    return render(request, 'dashboard-admin-pages/news-dashboard.html')

def direct_messages(request):
    return render(request, 'dashboard-admin-pages/contact.html')

def profile_dashboard(request):
    return render(request, 'dashboard-admin-pages/users-profile.html')

def help(request):
    return render(request, 'dashboard-admin-pages/help.html')








# ==== Students ==== 

