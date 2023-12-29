from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes')
    
    
    
    def __str__(self):
        return self.title