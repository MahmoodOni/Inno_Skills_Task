from django.db import models

class SimpleRecord(models.Model):
    # Basic fields
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/')
    
    # Size fields 
    name_size = models.FloatField(default=0)
    email_size = models.FloatField(default=0)
    phone_size = models.FloatField(default=0)
    file_size = models.FloatField(default=0)
    total_size = models.FloatField(default=0)
    
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name