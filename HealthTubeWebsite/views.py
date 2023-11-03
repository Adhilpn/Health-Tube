from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import Qnform,Qnform2,Qnform3,Qnform4,Qnform5,Qnform6,Userform,Qnform7
from .models import Ans1,Ans3,Ans2,Ans4,Ans5,Ans6,Ans7,CustomModelName
from .import models,forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def home(request):
    return render(request,'home.html')



#Views for member and admin sign up
def signUp(request):
    form=forms.SignUpForm()
    if request.method=="POST":
        form =forms.SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

    
            member_group = Group.objects.get_or_create(name='Member')
            member_group[0].user_set.add(user)

            return HttpResponseRedirect('/UserView')
    return render(request,'signup.html',{'form':form})




def signUpAdmin(request):
    form=forms.AdminSigupForm()
    if request.method=="POST":
        form =forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

    
            admin = Group.objects.get_or_create(name='Admin')
            admin[0].user_set.add(user)
            

            return HttpResponseRedirect('/AdminView')
    return render(request,'adminsignup.html',{'form':form})


#View for user view after login
@login_required(login_url='/signIn')
def User(request):
    return render(request,"UserView.html")


#View for checking if user is admin
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

#View for redirecting user to admin page or member page
@login_required(login_url='/signIn')
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('AdminView')
    else:
        return render(request,"UserView.html")

#View for admin page
@login_required(login_url='/signIn')
@user_passes_test(is_admin)
def Admin(request):
    userform=Userform()
    context = {"userform":userform}
    return render(request,"AdminView.html",context)

#View for member login
class LoginInterfaceView(LoginView):
    template_name='signIn.html'


#View for admin login
class LoginAdmin(LoginView):
    template_name='adminsignIn.html'


#View for logout
class LogoutInterfaceView(LogoutView):
    template_name='home.html'    



#Views for survey questions------------------------------------------------------------------------------
def Qn1(request):
    if request.method == 'POST':
        filled_form = Qnform(request.POST)
        if filled_form.is_valid():
            survey = filled_form.save()
            note = 'Great!Click here to proceed... '
            return redirect('qn2')

        else:
            note = 'please try again'
        new_form = Qnform()
        return render(request, 'qn1.html',{'qnform':new_form, 'note':note,'qnform':survey})
    else:
        form = Qnform()
        return render(request, 'qn1.html', {'qnform':form})
    

def Qn2(request):
    if request.method == 'POST':
        filled_form = Qnform2(request.POST)
        if filled_form.is_valid():
            survey = filled_form.save()
            note = 'Great!Click here to proceed... '
            return redirect('qn3')
            
        else:
            note = 'please try again'
        new_form = Qnform2()
        return render(request, 'qn2.html',{'qnform':new_form, 'note':note,'qnform':survey})
    else:
        form = Qnform2()
        return render(request, 'qn2.html', {'qnform':form})
    

def Qn3(request):
    if request.method == 'POST':
        filled_form = Qnform3(request.POST)
        if filled_form.is_valid():
            survey = filled_form.save()
            note = 'Great!Click here to proceed... '
            return redirect('qn4')
            
        else:
            note = ' please try again'
        new_form = Qnform3()
        return render(request, 'qn3.html',{'qnform':new_form, 'note':note,'qnform':survey})
    else:
        form = Qnform3()
        return render(request, 'qn3.html', {'qnform':form})
    
def Qn4(request):
    if request.method == 'POST':
        filled_form = Qnform4(request.POST)
        if filled_form.is_valid():
            survey = filled_form.save()
            
            note = 'Great!Click here to proceed... '
            return redirect('qn5')

        else:
            note = ' please try again'
        new_form = Qnform4()
        return render(request, 'qn4.html',{'qnform':new_form, 'note':note,'qnform':survey})
    else:
        form = Qnform4()
        return render(request, 'qn4.html', {'qnform':form})
    
def Qn5(request):
    if request.method == 'POST':
        filled_form = Qnform5(request.POST)
        if filled_form.is_valid():
            survey = filled_form.save()
            note = 'Great!Click here to proceed... '
            return redirect('qn7')
            
        else:
            note = ' please try again'
        new_form = Qnform5()
        return render(request, 'qn5.html',{'qnform':new_form, 'note':note,'qnform':survey})
    else:
        form = Qnform5()
        return render(request, 'qn5.html', {'qnform':form})
    
def Qn6(request):
    if request.method == 'POST':
        filled_form = Qnform6(request.POST)
        if filled_form.is_valid():
            survey = filled_form.save()
            note = 'Great!Click here to proceed... '
            return redirect('result')
            
        else:
            note = ' please try again'
        new_form = Qnform6()
        return render(request, 'qn6.html',{'qnform':new_form, 'note':note,'qnform':survey})
    else:
        form = Qnform6()
        return render(request, 'qn6.html', {'qnform':form})
    
def Qn7(request):
    if request.method == 'POST':
        filled_form = Qnform7(request.POST)
        if filled_form.is_valid():
            survey = filled_form.save()
            note = 'Great!Click here to proceed... '
            return redirect('qn6')
            
        else:
            note = ' please try again'
        new_form = Qnform7()
        return render(request, 'qn7.html',{'qnform':new_form, 'note':note,'qnform':survey})
    else:
        form = Qnform7()
        return render(request, 'qn7.html', {'qnform':form})
        
#---------------------------------------------------------------------------------------------------------------




#View for deleting survey questions
def delete(request):
    #deletes all objects from Car database table
    Ans1.objects.all().delete()   
    Ans2.objects.all().delete() 
    Ans3.objects.all().delete()   
    Ans4.objects.all().delete() 
    Ans5.objects.all().delete()   
    Ans6.objects.all().delete()  
    Ans7.objects.all().delete()  
    return render(request, 'new_survey.html')


#View for new survey
def survey(request):
   return render(request,"new_survey.html")


#View for result page
def result(request):
    result1=models.Ans1.objects.get()
    result2=models.Ans2.objects.get()
    result3=models.Ans3.objects.get()
    result4=models.Ans4.objects.get()
    result5=models.Ans5.objects.get()
    result6=models.Ans6.objects.get()
    result7=models.Ans7.objects.get()
    
    return render(request,'Result.html',{'result1':result1,'result2':result2,'result3':result3,'result4':result4,'result5':result5,'result6':result6,'result7':result7,'result2':result2})




#Views for meal plans    
def diabeticPlan(request):
   return render(request,"diabeticPlan.html")

def wellnessPlan(request):
   return render(request,"wellnessPlan.html") 

def vegPlan(request):
   return render(request,"vegPlan.html") 

def athletePlan(request):
   return render(request,"athletePlan.html")

def intPlan(request):
   return render(request,"intPlan.html")  






#Views for workout plans
def chest(request):
   return render(request,"chest.html") 
def biceps(request):
   return render(request,"biceps.html") 
def triceps(request):
   return render(request,"triceps.html") 
def back(request):
   return render(request,"back.html") 
def legs(request):
   return render(request,"legs.html") 
def shoulder(request):
   return render(request,"shoulder.html") 