import pandas as pd
from collections.abc import Iterable
from django.db import models
from account.models import SignUpModel
from django.db.models import Sum

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=25)
    class Meta :
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    quiz_file =  models.FileField(upload_to='quiz/' , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # this will add the date time of the quiz automatically whenever a new quiz is created 
    updated_at = models.DateTimeField(auto_now = True) # this will add the date time of the quiz when the quiz is updated

    class Meta:
        verbose_name_plural = 'Quizzes'

    def save(self):
        super().save()
        if self.quiz_file:
            self.import_quiz_from_excel()
    
    def import_quiz_from_excel(self):
        # read the excel file
        df = pd.read_excel(self.quiz_file.path)
        # iterate over the rows
        for index,row in df.iterrows():
            # extract data from questions options and correct answer column of the excel file
            question_col_text = row['Question']
            choice1 = row['A']
            choice2 = row['B']
            choice3 = row['C']
            choice4 = row['D']
            correct_ans = row['Answer']

            # creating the question object of the Question model
            question = Question.objects.get_or_create(quiz=self , question_text=question_col_text) # this question variable will contain a tuple 
            print(question)
            # creating choice object of the Choice model
            choice_1 = Choice.objects.get_or_create(question=question[0] , choice_text=choice1 , is_correct=correct_ans=='A')  #we have used question=question[0] because the above question varibale will return a tuple so we have accessed its first value using this way
            choice_2 = Choice.objects.get_or_create(question=question[0] , choice_text=choice2 , is_correct=correct_ans=='B')
            choice_3 = Choice.objects.get_or_create(question=question[0] , choice_text=choice3 , is_correct=correct_ans=='C')
            choice_4 = Choice.objects.get_or_create(question=question[0] , choice_text=choice4 , is_correct=correct_ans=='D')





class Question(models.Model):
    quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question ,  on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.question_text[:50]} {self.choice_text}"


class QuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE)
    user = models.ForeignKey(SignUpModel , on_delete=models.CASCADE)
    score = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}{self.quiz.title}"

class UserRank(models.Model):
    user = models.ForeignKey(SignUpModel , on_delete=models.CASCADE)
    rank = models.IntegerField()
    total_score = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return f"{self.user.username}{self.rank}"
    
def update_leaderboard():
    # Getting the sum of score for all users
    user_scores = QuizSubmission.objects.values('user').annotate(total_score = Sum('score')).order_by('-total-score')
    print(user_scores)
    
    # storing the value of user_score in different variables user_score will have two values user_id and total_score of the user
    rank = 1
    for entry in user_scores:
        user_id = entry['user']
        total_score = entry['total_score']

    user_rank , created = UserRank.objects.get_or_create(user=user_id)
    print(user_rank , created)
    user_rank.rank = rank
    user_rank.total_score = total_score
    user_rank.save()

    rank += 1

    
    