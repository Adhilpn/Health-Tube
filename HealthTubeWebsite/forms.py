from django import forms
from django.contrib.auth.models import User


from .models import qn1,Ans1,qn2,Ans2,Ans3,qn3,qn4,Ans4,qn5,Ans5,Ans6,qn7,Ans7


#Sign up forms for member and admin 
class SignUpForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['first_name','last_name','username','password']
     
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']




#Form for displaying current members and admins 
class Userform(forms.ModelForm):
    user=forms.ModelChoiceField(queryset=User.objects,empty_label=None,widget=forms.RadioSelect)
    class Meta:
        model = User
        fields={'user'}




#Question forms for survey 
class Qnform(forms.ModelForm):
    options=forms.ModelChoiceField(queryset=qn1.objects,empty_label=None,widget=forms.RadioSelect)
    class Meta:
        model = Ans1
        fields={'options'}

class Qnform2(forms.ModelForm):
    options=forms.ModelChoiceField(queryset=qn2.objects,empty_label=None,widget=forms.RadioSelect)
    class Meta:
        model = Ans2
        fields={'options'}

class Qnform3(forms.ModelForm):
    options=forms.ModelChoiceField(queryset=qn3.objects,empty_label=None,widget=forms.RadioSelect)
    class Meta:
        model = Ans3
        fields={'options'}

class Qnform4(forms.ModelForm):
    options=forms.ModelChoiceField(queryset=qn4.objects,empty_label=None,widget=forms.RadioSelect)
    class Meta:
        model = Ans4
        fields={'options'}

class Qnform5(forms.ModelForm):
    options=forms.ModelChoiceField(queryset=qn5.objects,empty_label=None,widget=forms.RadioSelect)
    class Meta:
        model = Ans5
        fields={'options'}


class Qnform7(forms.ModelForm):
    options=forms.ModelChoiceField(queryset=qn7.objects,empty_label=None,widget=forms.RadioSelect)
    class Meta:
        model = Ans7
        fields={'options'}

class Qnform6(forms.ModelForm):
    Name=forms.TextInput()
    class Meta:
        model = Ans6
        fields={'Name'}
        labels={'Name':'Name'}