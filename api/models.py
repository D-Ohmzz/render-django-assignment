from django.db import models

#Customer class
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30, default='+254798889503')



#Order class
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
     #   return self.customer + ' ' + self.item + ' ' + self.amount + ' ' + self.time 