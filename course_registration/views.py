from django.shortcuts import render,redirect,get_object_or_404
from .models import Course_Registration,UserModel
from.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home(request):
    course_li=[]
    course_list = Course_Registration.objects.all()
    for i in course_list:
        if UserModel.objects.filter(user = request.user,course=i):
            pass
        else:
            course_li.append(i)
    context = {'course_list':course_list,
               'course_li':course_li,}
    if len(course_li) ==0:
        messages.success(request, f"{request.user.username}have registered all the course that are available here")
    return render(request,'course_registration/home.html',context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        # print("working")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} your account has been created and now you can login!")
            return redirect('/')
    form = UserRegistrationForm()
    context = {
        'form':form,
        }
    return render(request,'course_registration/registration.html',context)

@login_required
def course_detail(request,pk):
    course = Course_Registration.objects.get(pk=pk)
    register_course,created = UserModel.objects.get_or_create(user = request.user,course=course)
    register_course.save()
    messages.success(request, f"{request.user.username} has successfully registered for the {course.course_name} course")
    return redirect('/')




@login_required
def registered_course(request):
    registered_course = UserModel.objects.filter(user=request.user)
    context={'registered_course':registered_course,}
    return render(request,'course_registration/course_register.html',context)


def delete_course(request,pk):
    item = UserModel.objects.get(id=pk)
    item.delete()
    return redirect('registered_course')
