# Generated by Django 3.2.7 on 2021-10-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_user_review_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]