from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator #new

# Modell für Aufgabe
class Task(models.Model):
    title = models.CharField(max_length=200)	# Name der Aufgabe
    text = models.TextField()					# Beschreibung
    deadline = models.DateField(default=timezone.now) # Deadline
    state = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])	# Stand (mind 0, max 100, 0 ist der Defaultwert)
	   
	# Methoden
    def publish(self):
        self.save()

    def __str__(self):
        return self.title