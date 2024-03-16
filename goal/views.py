from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib import messages
from goal.models import Salary, Expense, Goal
from datetime import datetime 
from django.http import JsonResponse
# from .models import Profile

# # Create your views here.

def progress(request):
    return render(request, 'mainbase.html')

def salary(request):
    if(request.method=="POST"):
        fix_salary=request.POST['fix_salary']
        var_salary=request.POST['var_salary']
        income=Salary(fix_salary=fix_salary,var_salary=var_salary)
        income.save()
        messages.success(request, "salary entered successfully")
        
    return render(request, 'salary.html')

def expense(request):
    if(request.method=="POST"):
        exp_name=request.POST['exp_name']
        fix_expense=request.POST['fix_expense']
        var_expense=request.POST['var_expense']
        kharcha=Expense(exp_name=exp_name,fix_expense=fix_expense,var_expense=var_expense)
        kharcha.save()
        messages.success(request, "expense entered successfully")
    return render(request, 'expense.html')

def goal(request):
    if(request.method=="POST"):
        goal_name=request.POST['goal_name']
        amount=request.POST['amount']
        goalDeadline=request.POST['goalDeadline']
        achieve=Goal(goal_name=goal_name, amount=amount, goalDeadline=goalDeadline, start_time=datetime.today())
        achieve.save()
        messages.success(request, "goal entered successfully")
    return render(request, 'goal.html')

# def goal_chart(request):
#     goals = Goal.objects.all()
#     goal_labels = [Goal.goal_name for goal in goals]
#     goal_amounts = [Goal.goal_amount for goal in goals]
#     goal_data = {
#         'labels': goal_labels,
#         'amounts': goal_amounts,
#     }
#     return render(request, 'goal_chart.html', {'goal_data': goal_data})

# def goal_chart_data(request):
#     goals = Goal.objects.all()
#     goal_labels = [goal.name for goal in goals]
#     goal_amounts = [goal.amount for goal in goals]
#     data = {
#         'labels': goal_labels,
#         'amounts': goal_amounts,
#     }
#     return JsonResponse(data)

