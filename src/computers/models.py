from django.db import models
from django.urls import reverse
# Create your models here.

class Computer(models.Model):
    Name = models.CharField(max_length=20)
    Years_of_usage = models.IntegerField()
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    
    def get_absolute_url(self):
        return reverse("computers:computer-detail", kwargs={"id":self.id})


