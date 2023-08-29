from django.shortcuts import render, redirect, get_object_or_404
from .forms import SendForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import Q
from .forms import SendForm, CommentForm, UserUpdateForm, ProfilePicForm
from .models import School, News, Comment, ipModel, Profile, Educationalcenter
# Create your views here.

def home(request):
    profile = Profile.objects.all()
    return render(request, 'home.html', {"profile": profile})

def schools(request):
    school = School.objects.all()
    context = {
        'school' : school
    }
    return render(request, 'school.html', context)

def school_detail(request, id):
    get_queryset = School.objects.all()
    get = get_object_or_404(School, id=id)

    context = {
        'get_queryset' : get_queryset,
        'get' : get
    }

    return render(request, 'school-detail.html', context)

def news(request):
    news = News.objects.all()
    context = {
        'news' : news
    }

    return render(request, 'news.html', context)

def course(request):
    courses = Educationalcenter.objects.all()
    return render(request, 'course.html', {'courses' : courses})

def course_details(request, id):
    get_course = Educationalcenter.objects.all()
    course   = get_object_or_404(Educationalcenter, id=id)

    context = {
        'get_course' : get_course,
        'course' : course
    }

    return render(request, 'course-details.html', context)

def about(request):
    return render(request, 'about.html')


    
def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

def new_detail(request, id):

    # Visit user

    
    # # ====== Add comment  ========
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.author = request.user
    #         comment.save()
    #         return redirect('comments:comment_list')
    # else:
    #     form = CommentForm()



    # self.object = self.get_object()
    # context = self.get_coontext_data(object=self.object)
    # ip = get_client_ip(self.request)
    # print(ip)
    # if ipModel.objects.filter(ip=ip).exists():
    #     print('ip already present')
    #     post_id = request.GET.get('post-id')
    #     print(post_id)
    #     post = News.objects.get(id=post_id)
    #     post.views.add(ipModel.objects.get(ip=ip))
    # else:
    #     ipModel.objects.create(ip=ip)
    #     post_id = request.GET.get('post-id')
    #     post = News.objects.get(id=post_id)
    #     post.views.add(ipModel.objects.get(ip=ip))
    
    
    # ip = get_ip(request)
    # u = User(first_name=ip)
    # print(ip)
    # result = User.objects.filter(Q(first_name__icontains=ip))
    # if len(result)==1:
    #     print('User exist')
    # elif len(result)>1:
    #     print('user exist more...')
    # else:
    #     u.save()
    #     print('user is unique')
    # count = User.objects.all().count()
    # print('users total', count)



    # ===== List Comments =======
    comments = Comment.objects.all()

    # ========  Take news from id  =========
    get_news = News.objects.all()
    news = get_object_or_404(News, id=id)

    context = {
        'get_news':get_news,
        'news' : news,
        'comments': comments,
    }

    return render(request, 'news-detail.html', context)
    

def contact(request):
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message from {name}',
                message,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False
            )
    else:
        form = SendForm()
    
    context = {'form': form}
    return render(request, 'contact.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password  = password)

        if user != None:
            auth_login(request, user)
            response = redirect('home')   
            response.set_cookie('cookies.authorization', str(user.id))
            return response

        else:

            messages.error(request, 'Username or password is not correct')
            response = render(request, 'login.html')        
            return response

    else:

        return render(request, 'login.html')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        for usernames in User.objects.all():
                if usernames.username == username:
                    return redirect('register')
                else:
                    if password == confirm_password:
                        if username == "" or len(username) < 2 or last_name == "": 
                            messages.error(request, 'Usename too short')
                            return redirect('register')
                        elif 8 > len(password):
                            messages.error(request, 'This password is too short. It must contain at least 8 characters.')
                            return redirect('register')
                        else:
                            user = User.objects.create_user(username=username, email=email, last_name=last_name, password=password) 
                            auth_login(request, user)
                            response = redirect(home) 
                            response.set_cookie('cookies.authorization', str(user.id))
                            user.save()
                            return response
    else:
        return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect('home')




def profile(request, id):
    profile = Profile.objects.all()
    if request.user.is_authenticated:
        profiles = User.objects.get(id=id)
        return render(request, 'profile.html', {"profiles": profiles, "profile" : profile})
    else:
        messages.success(request, ('You must logged in'))
        return redirect('home')



@login_required
def update_user(request):
    user = request.user
    user_img, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=user_img)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('home',)
    else:
        form = UserUpdateForm(instance=user)
        profile_form = ProfilePicForm(instance=user_img)

    context = {
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'update_user.html', context)


