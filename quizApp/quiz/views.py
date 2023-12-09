from django.shortcuts import render , HttpResponseRedirect
from .models import Quiz , Category
from django.db.models import Q
from account.models import SignUpModel


# Create your views here.
def allquiz(request):
    if request.user.is_authenticated:
        profile = SignUpModel.objects.get(username=request.user)

        quizzes = Quiz.objects.order_by("-created_at")
        categories = Category.objects.all()
        return render(request, 'allquiz.html' ,{"quizzes":quizzes  , "categories":categories , "profile":profile})
    else:
        return HttpResponseRedirect('/signin/')

def search(request , category):
    if request.user.is_authenticated:
        profile = SignUpModel.objects.get(username=request.user)
    
        # search by Search Bar
        if request.GET.get('q') != None:
            q = request.GET.get('q')
            print(q)
            quizzes = Quiz.objects.filter(Q(title__icontains=q) | Q(description__icontains=q)).order_by('-created_at')

        # search by category
        elif category != " ":
            quizzes = Quiz.objects.filter(category__category_name=category).order_by('-created_at')
            # print(quizzes)
            # print(type(quizzes))
        
        else:
            quizzes = Quiz.objects.order_by("-created_at")

        categories = Category.objects.all()
        return render(request , 'allquiz.html' ,{"quizzes":quizzes ,"categories":categories , "profile":profile})
    else:
        return HttpResponseRedirect('/signin/')


# single quiz page view
def quiz(request , quiz_id):
    if request.user.is_authenticated:
        profile = SignUpModel.objects.get(username=request.user)
        # quiz = Quiz.objects.filter(id=quiz_id)
        # print(quiz)
        quiz = Quiz.objects.filter(id=quiz_id).first()
        print(quiz)
        return render(request , 'quiz.html' , {"quiz":quiz , "profile":profile} )
    else:
        return HttpResponseRedirect('/signin/')