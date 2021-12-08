from django.db import models

class Vendor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_vendor_by_email(email):
        try:
            return Vendor.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if Vendor.objects.filter(email = self.email):
            return True
        else:
            return False
