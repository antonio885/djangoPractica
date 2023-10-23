from django.db import models


# Create your models here.
class superheroe(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    nombre_superheroe = models.TextField(null=True, verbose_name='Nombre del heroe')
    ciudad = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)


    def __str__(self):
      fila = "titulo" + self.nombre + "apellido" + self.apellido + "nombreheroe" + self.nombre_superheroe+ "ciudad" + self.ciudad 
      return fila

    def delete(self, using= None, keep_parents=False):
       self.imagen.storage.delete(self.imagen.name)
       super().delete()
    
  