from django.contrib import admin

# Register your models here.
from .models import Clients,Courses
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name','t_id','language']
    list_per_page = 10
    list_max_show_all = 15
    list_filter = ['course']
    search_fields = ['name','t_id','phone','course__name','language']
    search_help_text = "Enter key word for searching"
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name','teacher','cost']
    list_filter = ['teacher','cost','started']
    list_per_page = 10
    list_max_show_all = 15
    search_fields = ['name','description','teacher','cost']

