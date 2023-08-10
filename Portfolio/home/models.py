from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    firm_name=models.CharField(max_length=250)
    contact_number=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return "{}-{}".format(self.name,self.firm_name)
    