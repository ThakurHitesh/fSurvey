import datetime
import uuid
from django.db import models
from django.utils import timezone

class TimeStamp(models.Model):
    """
    TimeStamp abstract model for storing basic timestamps
    """
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    modified_at = models.DateTimeField(db_index=True, auto_now=True)
    class Meta:
        abstract = True

class Question(TimeStamp):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.question_text


class Choice(TimeStamp):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
