from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import TemplateView,ListView
from myapp.forms import Loginform,ProfileForm
from myapp.models import Profile,Questions
import datetime
# Create your views here.
def hello(request):
        today=datetime.datetime.now().date()
        days=['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
        return render(request,"template1.html",{"today":today,"days":days})
    
def morning(request):
    text2="""<h2>Good Morning</h2>"""
    return redirect("https://www.tutorialspoint.com/django/django_page_redirection.htm")

def article(request,articleid,year):
    test="Displaying article number: %s    %s"%(articleid,year)
    return HttpResponse(test)

def sendemail(request,emailto):
    mes1=send_mail("For education","How are your studies going?","shahpriyamh@gmail.com",[emailto],fail_silently=False)
    return HttpResponse("%s"%mes1)

class ArticleView(TemplateView):
    template_name="static.html"
    
class Dreamreal(ListView):
    template_name="dreamreal_list.html"
    
def login(request):
    username='not logged in'
    if request.method=="POST":
        MyLoginForm=Loginform(request.POST)
        if MyLoginForm.is_valid():
            username=MyLoginForm.cleaned_data['username']
            MyLoginForm.save()
        else:
            for obj in MyLoginForm.errors:
                print(obj)
    else:
        MyLoginForm=Loginform()
    
    return render(request,'loggedin.html',{'username':username}) 

def SaveProfile(request):
    saved=False
    if request.method=='POST':
        MyProfileForm=ProfileForm(request.POST,request.FILES)
        if MyProfileForm.is_valid():
            profile=Profile()
            profile.name=MyProfileForm.cleaned_data["name"]
            profile.picture=MyProfileForm.cleaned_data["picture"]
            profile.save()
            saved=True
    else :
        MyProfileForm=ProfileForm()
    return render(request,'saved.html',locals())


def QuestionView(request,pkd):
    return render(request,"login.html",{"question":Questions.objects.get(pk=pkd).question,"pk":pkd})