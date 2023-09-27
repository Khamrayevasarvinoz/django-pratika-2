from django.urls import path 
from .views import * 
urlpatterns = [
    path('', index, name='index'),
    path('/meetings', meetings, name='meetings'),
    path('/meetingdetail', meetingdetail , name='meetingdetail'),
    path('/seem', seem , name='seem'),
    path('/teacher', teacher , name='teacher'),
    path('/education', education , name='education')
]
