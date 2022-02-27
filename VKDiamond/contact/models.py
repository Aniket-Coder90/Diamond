import uuid
from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.EmailField(blank=False)
    ContactNo = models.IntegerField()
    TextMessage = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.Firstname} {self.Lastname}'