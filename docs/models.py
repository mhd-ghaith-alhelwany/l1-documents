from django.db import models
from datetime import datetime


# Create your models here.
class Document(models.Model):
    file_name = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.file_name


# Create your models here.
class Table(models.Model):
    title = models.CharField(max_length=200)
    json = models.CharField(max_length=5000)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return self.title