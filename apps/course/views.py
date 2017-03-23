from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = { 'courses' : Course.objects.all()}
	return render(request, 'course/index.html', context)
def add(request):
	Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
	return redirect('/')
def remove(request, id):
	context = { 'course' : Course.objects.get(id=id)
	}
	return render(request, "course/deluser.html", context)
def confirmrm(request, id):
	this = Course.objects.get(id=id)
	this.delete()
	return redirect('/')
