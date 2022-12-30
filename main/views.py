from django.shortcuts import render,HttpResponseRedirect
from main.models import StudentModel
from main.forms import StudentForm
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Create your views here.


class Show_Add(TemplateView):
    def get (self,request):
        fm=StudentForm()
        stud=StudentModel.objects.all()
        context={'fm':fm,'students':stud}
        return render(request,'main/addstudent.html',context)
    
    def post(self,request):
        fm=StudentForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            su=StudentModel(name=name,email=email,password=password)
            su.save()
            return HttpResponseRedirect('/add/')



'''def add_student_show(request):
    if request.method=="POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            su=StudentModel(name=name,email=email,password=password)
            su.save()
    fm=StudentForm()
    students=StudentModel.objects.all()
    context={
        "fm":fm,
        "students":students
    }
    return render(request,'main/addstudent.html',context)'''

class DeleteUser(RedirectView):
    url='/add/'
    def get_redirect_url(self ,*args,**kwargs):
        pk=kwargs['pk']
        su=StudentModel.objects.get(pk=pk)
        su.delete()
        return super().get_redirect_url(*args,**kwargs)


'''def delete(request,pk):
    if request.method=="POST":
        student=StudentModel.objects.get(pk=pk)
        student.delete()
    return HttpResponseRedirect('/add')'''

class UpdateUser(View):
    def get(self,request,pk):
        pi=StudentModel.objects.get(pk=pk)
        fm=StudentForm(instance=pi)
        context={
            "fm":fm
        }
        return render(request,'main/update.html',context)
    def post(self,request,pk):
        pi=StudentModel.objects.get(pk=pk)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/add/')


'''def update_data(request,pk):
    pi=StudentModel.objects.get(pk=pk)
    if request.method=="POST":
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/add/')
    else:
        fm=StudentForm(instance=pi)
        context={"fm":fm}
        return render(request,'main/update.html',context)'''

        


        

