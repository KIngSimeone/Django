from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name
    
    def __str__(self):
        return self.last_name

    def __str__(self):
        return self.email
