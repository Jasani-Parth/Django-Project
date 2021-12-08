from django.db import models

class Transporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_transporter_by_email(email):
        try:
            return Transporter.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if Transporter.objects.filter(email = self.email):
            return True
        else:
            return False

    def get_random():
        return Transporter.objects.order_by("?").first()
