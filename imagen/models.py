from django.db import models
import os
class Image(models.Model):
    title = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes')
    
    def delete(self , *args , **kwargs):
        file_path = self.imagen.path
        
        super().delete(*args, **kwargs)
        
        if file_path and os.path.isfile(file_path):
            print(f' Eliminando archivo', {file_path})
            os.remove(file_path)
        
    
    def __str__(self):
        return self.title