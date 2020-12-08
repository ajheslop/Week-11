from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    #127.0.0.1/polls
    path('', views.index, name='index'),
    #127.0.0.1/polls/2 (now shows an ID after polls)
    path('<int:question_id>/', views.detail, name='detail'),
    #127.0.0.1/polls/1/results (now shows an ID after polls with results page)
    path('<int:question_id>/results/', views.results, name='results'),
    #127.0.0.1/polls/1/vote (now shows an ID after polls with a vote page)
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]