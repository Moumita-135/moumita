from django.contrib import admin
from django.urls import path
from account import views
admin.site.site_header = "CDC ADMIN"
admin.site.site_title = "CDC ADMIN"
admin.site.index_title ="TECH DISCUSSION FORUM"

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signup/signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('cdc/', views.cdc, name='cdc'),
    path('index1/', views.index1, name='index1'),
    path('index2/', views.index2, name='index2'),
    path('about1/', views.about1, name='about1'),
    path('about2/', views.about2, name='about2'),
    path('contact1/', views.contact1, name='contact1'),
    path('contact2/', views.contact2, name='contact2'),
    path('category1/', views.category1, name='category1'),
    path('category2/', views.category2, name='category2'),
    path('domain/', views.domain, name='domain'),
    path('recent question/', views.recentquestion, name='recent question'),
    path('GATE/', views.GATE, name='GATE'),
    path('INTERVIEW/', views.INTERVIEW, name='INTERVIEW'),
    path('most answer/', views.mostanswer, name='most answer'),
    path('answers/', views.answers, name='answers'),
    path('no answer/', views.noanswer, name='no answer'),
    path('most visited/', views.mostvisited, name='most visited'),
    path('ECE/', views.ECE, name='ECE'),
    path('CSE/', views.CSE, name='CSE'),
    path('EE/', views.EE, name='EE'),
    path('CE/', views.CE, name='CE'),
    path('ME/', views.ME, name='ME'),
    path('addquestion1/', views.addquestion1, name='addquestion1'),
    path('addquestion2/', views.addquestion2, name='addquestion2'),
    path('Allquestion1/', views.allquestion1, name='allquestion1'),
    path('allquestion2/', views.allquestion2, name='allquestion2'),
    path('answersubmit/<int:pk>/<int:fk>', views.answersubmit, name='answersubmit'),
    



]
