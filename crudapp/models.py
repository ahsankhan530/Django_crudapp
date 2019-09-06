from django.db import models

class registrations(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=20)
    email=models.EmailField()
    econtact=models.CharField(max_length=15)
    econtact=models.CharField(max_length=100)

    class Meta:
        db_table="Registartion"