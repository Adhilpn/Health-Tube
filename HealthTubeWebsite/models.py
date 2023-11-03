from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomModelName(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) # instead of user_id = IntegerField()

#Models for storing survey questions
class qn1(models.Model):
    title= models.CharField(max_length=255)
    def __str__(self) :
        return self.title

class qn2(models.Model):
    title= models.CharField(max_length=255)
    def __str__(self) :
        return self.title
    
class qn3(models.Model):
    title= models.CharField(max_length=255)
    def __str__(self) :
        return self.title

class qn4(models.Model):
    title= models.CharField(max_length=255)
    def __str__(self) :
        return self.title
    
class qn5(models.Model):
    title= models.CharField(max_length=255)
    def __str__(self) :
        return self.title

class qn7(models.Model):
    title= models.CharField(max_length=255)
    def __str__(self) :
        return self.title



#Models for storing survey answers
class Ans1(models.Model):
    options = models.ForeignKey(qn1,on_delete=models.CASCADE,)
    def __str__(self) :
        return self.options
    
class Ans2(models.Model):
    options = models.ForeignKey(qn2,on_delete=models.CASCADE,)
    def __str__(self) :
        return self.options
    
class Ans3(models.Model):
    options = models.ForeignKey(qn3,on_delete=models.CASCADE,)
    def __str__(self) :
        return self.options
    
class Ans4(models.Model):
    options = models.ForeignKey(qn4,on_delete=models.CASCADE,)
    def __str__(self) :
        return self.options

class Ans5(models.Model):
    options = models.ForeignKey(qn5,on_delete=models.CASCADE,)
    def __str__(self) :
        return self.options
    
class Ans7(models.Model):
    options = models.CharField(max_length=255)
    def __str__(self) :
        return self.options
    
class Ans6(models.Model):
    Name = models.CharField(max_length=255)
    def __str__(self) :
        return self.Name