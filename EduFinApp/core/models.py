from django.db import models

class Testing(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    DateTimeField=models.TextField(auto_now_add=True)

    def __str__(self):
        return self.name