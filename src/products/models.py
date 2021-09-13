from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    Description = models.TextField(blank=True, null=True)
    Price=models.DecimalField(decimal_places=2, max_digits=10000, default = False)
    summary=models.TextField(blank=False, null=True)
    Deciding=models.BooleanField(default = False)
    
    def get_absolute_url(self):
        #creating dynamic url 1-st way:
        return reverse("dynamic_redirecting", kwargs={"my_id": self.id})
        #creating dynamic url 2-nd way:
        # return (f"/dynamic_linking/{self.id}/")

    def get_url(self):
        return reverse("products:product-detail", kwargs={"my_id": self.id})