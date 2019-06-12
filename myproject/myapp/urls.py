from django.urls import path
from myapp.views import hello
from myapp.views import morning
from myapp.views import article,sendemail,ArticleView,Dreamreal,login,SaveProfile,QuestionView
from django.views.generic import TemplateView,ListView
from myapp.models import Reporter
urlpatterns = [
    path('hello/',hello,name='hello' ),
    path('morning/', morning , name='morning'),
    path('article/<int:articleid>/<int:year>',article,name='article'),
    path('sendemail/(?P<emailto>[\w.%+-]+@[a-z]{0-10}+.[a-z]{2-4})/',sendemail,name='email'),
    path('template/',ArticleView.as_view()),
    path('dreamlist/',Dreamreal.as_view(model=Reporter,context_object_name="Dreamreal_objects")),
    path('connection/',TemplateView.as_view(template_name='login.html')),
    path('login/',login,name='login'),
    path('profile/',TemplateView.as_view(template_name='profile.html')),
    path('saved/',SaveProfile,name='SaveProfile'),
    path('question/<int:pkd>/',QuestionView,name='Question'),
]