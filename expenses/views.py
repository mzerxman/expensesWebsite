from django.shortcuts import render
from . import views

# Create your views here.

def index(request):

	return render(request, 'expenses/index.html')


def add_expense(request):

	return render(request, 'expenses/add_expense.html')


