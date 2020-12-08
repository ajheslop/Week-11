from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
# return the question text in the API Shell
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
# return the question text in the API Shell
     
    def __str__(self):
        return self.choice_text