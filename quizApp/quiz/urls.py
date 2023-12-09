from django.urls import path
from . import views

urlpatterns = [
    path('allquiz/',views.allquiz , name="allquiz"),
    path('search/<str:category>/' , views.search , name="search"),
    path('quiz/<int:quiz_id>/',views.quiz , name="quiz"),


]
