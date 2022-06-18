from django.urls import  path
from .views import  *
urlpatterns = [
    path('courses',get_all_courses),
    path('course/<int:id>',get_course),
    path('create/<int:t_id>/<str:name>/',createuser),
    path('setlang/<int:t_id>/<str:language>/',setuserlang),
    path('setphone/<int:t_id>/<str:phone>/',setuserphone),
    path('setcourse/<int:t_id>/<int:course>/', setusercourse),
    path('getlang/<int:t_id>',getlang),
    path('getcourse/<int:t_id>',getcourse),
    path("coursemember/<int:course>",getcoursemembers)

]