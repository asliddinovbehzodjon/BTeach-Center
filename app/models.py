from django.db import models
class Courses(models.Model):
    name = models.CharField(max_length=500,verbose_name="Course name",help_text="Enter course name")
    description = models.TextField(verbose_name="Course description",help_text="Enter course description")
    image = models.ImageField(upload_to="course-images",verbose_name="Course image",help_text="Enter course image")
    teacher = models.CharField(max_length=500,verbose_name="Course teacher",help_text="Enter course teacher")
    cost = models.PositiveIntegerField(verbose_name="Course price",help_text="Enter course price")
    started = models.DateTimeField(verbose_name="Beginning of the course",help_text="Enter beginning of the course")
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Course"
        verbose_name = "Course "
        verbose_name_plural = "Courses "
# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True,verbose_name="User Fullname",help_text="Enter user name")
    t_id = models.IntegerField(verbose_name="User Telegram Id",help_text="Enter user telegram id")
    language = models.CharField(max_length=10,default='uz',verbose_name="User System Language",help_text='Enter system language')
    phone = models.CharField(max_length=500,verbose_name="User phone number",help_text="Enter user phone number",null=True,blank=True)
    course = models.ManyToManyField(Courses,verbose_name="Courses",related_name="kurslar",help_text="Enter chosen courses",null=True,blank=True)
    adress = models.CharField(max_length=500,verbose_name="User address",help_text="Enter user address",null=True,blank=True)
    @property
    def get_courses(self):
        kurslar = self.course_set.all()
        return kurslar
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Clients"
        verbose_name = "Client "
        verbose_name_plural = "Clients "

