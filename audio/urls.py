from django.urls import path
from . import views

urlpatterns = [

    path('', views.index , name= "index"),
    path('profile/<str:sk>/',views.studentprofile, name="studentprofile"),
    path('enroll', views.enroll, name="enroll"),
    path('dashboard_telugu', views.dashboard, name="dashboard"),
    path('schedules', views.schedules, name="schedules"),
    path('schedule', views.schedule, name="schedule"),
    # path('reschedule', views.reschedule, name="reschedule"),
    path('appointment', views.appointment,name="appointment"),
    path('letsmakefun', views.letsmakefun, name= "letsmakefun"),
    path('audio', views.audio_player, name="audio_player"),
    path('dictationaudio', views.dictationaudio,name="dictationaudio"),
    path('statusupdate', views.statusupdate,name="statusupdate"),
    path('testinputs', views.testinputs, name="testinputs"),
    path('profile/<str:sk>/marksinit', views.marksinit, name="marksinit"),
    path('profile/<str:sk>/marksupdate', views.marksupdate, name="marksupdate"),

    # path('download/<int:id>', download_view)
    # path('enroll', views.student_enroll, name="enroll"),
]