from django.contrib import admin
from .models import School, Subject, Course, Educationalcenter, Teachers, News, Comment, Profile, ipModel
from django.contrib.auth.models import Group, User

# Move Profiles inline to User
class ProfileInline(admin.StackedInline):
    model = Profile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", 'last_name', 'email', 'password',]
    inlines = [ProfileInline]
    list_display = ('id', 'username', 'password', )

# Unregister initial User  
admin.site.unregister(User)

# Register User
admin.site.register(User, UserAdmin)



@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director', )

admin.site.register(Subject)
admin.site.register(Course)


@admin.register(Educationalcenter)
class EducationallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_center', 'director', )
    filter_horizontal = ['courses']



admin.site.register(Teachers)
admin.site.register(News)
admin.site.register(Comment) 
admin.site.register(ipModel)


admin.site.unregister(Group)