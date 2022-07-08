from django.db import models

# Create your models here.

class lib(models.Model):
    book_name=models.CharField(max_length=40)
    published_year=models.IntegerField()
    price=models.BigIntegerField()

    def __str__(self):
        return self.book_name