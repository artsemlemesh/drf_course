from django.db import models

class MyName(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    alive = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + str(self.alive)