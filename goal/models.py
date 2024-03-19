from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Salary(models.Model):
    user = models.CharField(max_length=100)
    fix_salary = models.IntegerField(null=False, blank=False)
    var_salary = models.IntegerField(null=False, blank=False)
    
    # def __str__(self):
    #     return self.name
    

class Expense(models.Model):
    user = models.CharField(max_length=100)
    exp_name = models.CharField(max_length=100,null=False, blank=False)
    fix_expense = models.IntegerField(null=False, blank=False)
    var_expense = models.IntegerField(null=False, blank=False)
    # def __str__(self):
    #     return self.name

class Goal(models.Model):
    user = models.CharField(max_length=100)
    goal_name=models.CharField(max_length=100,null=False, blank=False)
    amount=models.IntegerField(null=False, blank=False)
    goalDeadline=models.DateField(null=False, blank=False)
    start_time=models.DateField()
    # def __str__(self):
    #     return self.name

