from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class land(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    contact_number = models.CharField(max_length=20,  null=True,# Adjust based on your needs
        validators=[
            RegexValidator(                
                regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    square_footage = models.IntegerField(default=0)
    image = models.FileField( blank=True,null=True,upload_to='property_image/')

    def __str__(self):
        return self.owner
