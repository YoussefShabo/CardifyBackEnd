from django.db import models
from django import forms

# Create your models here.
SUBJECT_CHOICES = [
    ('math', 'Math'),
    ('science', 'Science'),
    ('scoial', 'Scoial Studies'),
    ('english', 'English'),
]
class Deck(models.Model):
    title = models.CharField(max_length=32)
    subject = models.CharField(choices=SUBJECT_CHOICES, default='math')
    comments = models.CharField()

class Card(model.Models):
    deck = models.ForeignKey(Deck)
    question = models.CharField()
    answer = models.CharField()
    image = models.CharField()
