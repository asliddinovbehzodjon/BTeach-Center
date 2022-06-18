from django.shortcuts import render,get_object_or_404
from .models import Clients,Courses
from django.http import JsonResponse
# Create your views here.
def get_all_courses(requests):
    courses = Courses.objects.all().values()
    return JsonResponse(list(courses),safe=False)
def get_course(request,id):
    course = Courses.objects.filter(id=id).values()
    return JsonResponse(list(course),safe=False)
def createuser(request,name,t_id):
    if Clients.objects.filter(t_id = t_id).exists():
        Clients.objects.filter(t_id=t_id).update(name = name)
        return JsonResponse({"data":"User Already created"},safe=False)
    else:
        Clients.objects.create(t_id = t_id,name = name)
        return JsonResponse({"data":"User created"},safe=False)
def setuserlang(request,language,t_id):
    if Clients.objects.filter(t_id = t_id).exists():
        Clients.objects.filter(t_id=t_id).update(language =  language)
        return JsonResponse({"data":"User Already created"},safe=False)
    else:
        Clients.objects.create(t_id = t_id,language=language)
        return JsonResponse({"data":"User created"},safe=False)
def setuserphone(request,phone,t_id):
    if Clients.objects.filter(t_id = t_id).exists():
        Clients.objects.filter(t_id=t_id).update(phone = phone)
        return JsonResponse({"data":"User Already created"},safe=False)
    else:
        Clients.objects.create(t_id = t_id,phone=phone)
        return JsonResponse({"data":"User created"},safe=False)
def setusercourse(request,course,t_id):
    if Clients.objects.filter(t_id = t_id).exists():
        kurs = get_object_or_404(Courses,id=course)

        client = Clients.objects.get(t_id=t_id)
        client.course.add(kurs)
        client.save()
        return JsonResponse({"data":"User added to this course"},safe=False)
    else:
        Clients.objects.create(t_id = t_id,course=course)
        return JsonResponse({"data":"User created"},safe=False)
# Get System Language
def getlang(request,t_id):
    user = Clients.objects.filter(t_id = t_id).values()
    data = list(user)
    return JsonResponse({"data":data},safe=False)
def getcourse(request,t_id):
    user = get_object_or_404(Clients,t_id=t_id)
    data = user.course.all().values()
    return JsonResponse({"data": list(data)}, safe=False)
def getcoursemembers(request,course):
    kurs = get_object_or_404(Courses,id=course)
    data = kurs.kurslar.all().values()
    return JsonResponse({"data": list(data)}, safe=False)
