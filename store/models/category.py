from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def get_category_by_name(name):
        return Category.objects.get(name=name)

    def __str__(self):
        return self.name