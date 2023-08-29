from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(blank=False, null=True )
    user_img = models.ImageField('Фотография Пользователя', blank = True, upload_to='img-user')


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользовательи'

class Teachers(models.Model):
    name = models.CharField('Имя',max_length=100, db_index=True)
    last_name = models.CharField('Фамилия',max_length=100)
    img  = models.ImageField('Фотография',blank=False, upload_to='img-teachers/')
    phone_number = PhoneNumberField()
    date_of_birth = models.DateTimeField('Дата Рождение',blank=False)
    email = models.EmailField(blank=False)
    course_teahcer = models.ForeignKey('Course', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителья'




class School(models.Model):
    title = models.CharField(max_length=50, blank=False, db_index=True)
    about_school = models.TextField(max_length=500, blank=False)
    director = models.CharField('Директор',max_length=100, blank=False)
    school_img = models.ImageField(blank=False, upload_to='school-img/')
    director_img = models.ImageField(blank=False, upload_to='school_director_img', null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'




class Subject(models.Model):
    title = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'





class ipModel(models.Model):
    ip = models.CharField(max_length=255)

    def __str__(self):
        return self.ip 






class News(models.Model):
    title = models.CharField('Краткое название', max_length=50, blank=False)
    news_img = models.ImageField('Фоторафия для новости', upload_to='news-img', null=True)
    information = models.TextField(verbose_name='иформация', blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    views = models.ManyToManyField(ipModel, related_name='просмотры', blank=True)

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



class Educationalcenter(models.Model):
    name_center = models.CharField('Название центра', max_length=50, blank=False)
    img_center = models.ImageField('Фотография центра', blank=False, upload_to='img-center/')
    about_center = models.TextField('Иформация о Центре', blank=False)
    director = models.CharField('Директор', max_length=70, blank=False)
    director_img = models.ImageField('Фотография Директора')
    courses = models.ManyToManyField('Course', blank=False, related_name='Курсы')

    def __str__(self):
        return self.name_center

    class Meta:
        verbose_name = 'Учебный Центр'
        verbose_name_plural = 'Учебные Центры'




class Course(models.Model):
    title = models.CharField(max_length=50, blank=False)
    info_course = models.TextField('Информация о Курсе', blank=False)
    img = models.ImageField('Фотография для курса', blank=False, upload_to='img-course/')

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'





class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.author, self.name)

    class Meta:
        verbose_name_plural = 'Комент'



    