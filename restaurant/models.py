from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    reservation_date = models.DateField()

    def __str__(self): 
        return self.name

class MenuItem(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2)
   inventory = models.IntegerField()
   
   def get_item(self):
    return f'{self.title} : {str(self.price)}'
   
   def __str__(self):
    return f'{self.title} : {str(self.price)}'