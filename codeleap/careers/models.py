from django.db import models

# Create your models here.
class Career(models.Model):
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    titlle = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    

    def __str__(self):
        return f'{self.id} - {self.username} : {self.title}'