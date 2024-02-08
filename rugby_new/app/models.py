from django.db import models

# Create your models here.
class Player(models.Model):
    """_summary_
    :arg

    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self,):
        return f"{self.first_name} - {self.last_name}"
