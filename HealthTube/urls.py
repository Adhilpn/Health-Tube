"""
URL configuration for HealthTube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HealthTubeWebsite import views

from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),

    #urls for sign in and sign up
    path('signup/',views.signUp,name='signup'),
    path('adminsignUp/',views.signUpAdmin,name='adminsignUp'),
    path('signIn/',views.LoginInterfaceView.as_view()),
    path('adminsignIn/',views.LoginAdmin.as_view()),
    path('AdminView/',views.Admin),
    path('verification/',views.afterlogin_view),

    path('logout/',views.LogoutInterfaceView.as_view()),
    path('UserView/',views.User),


    #urls for survey questions
    path('qn1/',views.Qn1,name='qn1'),
    path('qn2/',views.Qn2,name='qn2'),
    path('qn3/',views.Qn3,name='qn3'),
    path('qn4/',views.Qn4,name='qn4'),
    path('qn5/',views.Qn5,name='qn5'),
    path('qn6/',views.Qn6,name='qn6'),
    path('qn7/',views.Qn7,name='qn7'),
 
    

    path('delete/',views.delete,name='delete'),
    path('new_survey/',views.survey,name='new_survey'),
    path('result/',views.result,name='result'),

    #urls for meal plans
    path('diabeticPlan/',views.diabeticPlan,name='diabeticPlan'),
    path('wellnessPlan/',views.wellnessPlan,name='wellnessPlan'),
    path('vegPlan/',views.vegPlan,name='vegPlan'),
    path('athletePlan/',views.athletePlan,name='athletePlan'),
    path('intPlan/',views.intPlan,name='intPlan'),

    #urls for workout plans
    path('chest/',views.chest,name='chest'),
    path('legs/',views.legs,name='legs'),
    path('back/',views.back,name='back'),
    path('triceps/',views.triceps,name='triceps'),
    path('biceps/',views.biceps,name='biceps'),
    path('shoulder/',views.shoulder,name='shoulder'),
    
]
