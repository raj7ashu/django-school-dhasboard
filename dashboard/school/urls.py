from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.home_view,name=''),
    path('adminclick',views.adminclick_view),
    path('studentclick',views.studentclick_view),
    path('teacherclick',views.teacherclick_view),


]