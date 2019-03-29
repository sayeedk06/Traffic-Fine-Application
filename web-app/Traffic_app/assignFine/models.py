from django.db import models
from django.conf import settings
# Create your models here.
class Fine(models.Model):
    """docstring forFine."""
    amount = models.PositiveIntegerField()
    numberPlate = models.CharField(max_length=50)
    policeUsername = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.numberPlate
