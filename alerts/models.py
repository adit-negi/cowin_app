from django.db import models

# Create your models here.
class Visitor(models.Model):
    name =models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank =True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    last_sent = models.DateTimeField(null=True, blank=True)
    registration_mail_sent = models.BooleanField(blank=True, default=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "visitor"
        verbose_name = 'Visitor'
        verbose_name_plural = "Visitors"

#cowin_bot_production