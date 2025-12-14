from django.db import models

# Create your models here.
from django.db import models

class MuscleGroup(models.TextChoices):
    CHEST = 'CHEST', 'Chest'
    BACK = 'BACK', 'Back'
    LEGS = 'LEGS', 'Legs'
    CORE = 'CORE', 'Core'

class DifficultyLevel(models.TextChoices):
    BEGINNER = 'BEGINNER', 'Beginner'
    INTERMEDIATE = 'INTERMEDIATE', 'Intermediate'
    ADVANCED = 'ADVANCED', 'Advanced'

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(
        max_length=20,
        choices=MuscleGroup.choices
    )
    difficulty = models.CharField(
        max_length=20,
        choices=DifficultyLevel.choices
    )