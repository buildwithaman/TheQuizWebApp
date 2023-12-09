from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('register/', views.register , name="register"),
    path('signin/',views.signin , name='signin'),
    path('leaderboard/' , views.leaderboard , name='leaderboard'),
    path('signout/',views.signout , name="signout"),
    path('profile/<str:username>' , views.profile , name='profile'),
    
]

