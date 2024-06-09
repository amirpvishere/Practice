from django.shortcuts import render
from .models import Course

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'course_app/courses_list.html', context={"courses": courses}) 


def courses(request):
    return render(request, 'course_app/courses.html')


def details(request, id):
    courses = Course.objects.get(id=id)
    courses.views += 1
    if courses.availablity == True: 
        courses.availablity = False
    else: 
        courses.availablity = True
    courses.save()
    return render(request, 'course_app/courses_detail.html', context={"courses": courses})


def add_course(request):
    if request.method == "GET":
        title = request.GET.get("title")
        description = request.GET.get("description")
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
    
    if title and description:
            Course.objects.create(title=title, description=description)
    
    return render(request, "course_app/courses_add.html", context={"course": courses})





