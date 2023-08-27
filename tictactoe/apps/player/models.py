from django.db import models

class Player(models.Model):

    username = models.CharField("Username", max_length=40)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Username"
