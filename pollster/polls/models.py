from django.db import models

class Question(models.Model):  #models.Model - To inherit all the methods from it
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("Date published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #CASCADE - choices also be deleted on deleting the question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text