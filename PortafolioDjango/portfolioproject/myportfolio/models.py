from django.db import models
from .utils import encrypt_message, decrypt_message
from ckeditor.fields import RichTextField

# Create your models here.
#myportfolio/models.py

# Modelo para las categorías de los proyectos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
# Modelo para las tecnologías utilizadas en los proyectos
class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
    #Modelo para los proyectos del portafolio
class Proyecto(models.Model):
        titulo = models.CharField(max_length=200)
        imagen = models.ImageField(upload_to='proyectos/')
        descripcion = models.TextField()
        contenido = RichTextField()
        tecnologias = models.ManyToManyField(Tecnologia)
        link_sitio = models.URLField(max_length=200)
        link_repositorio = models.URLField(max_length=200)
        Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

        def __str__(self):
            return self.titulo   

#models.py  archivo
#modelos del formulario

class Contacto(models.Model):
     nombre = models.CharField(max_length=100)
     email = models.EmailField()
     mensaje = models.TextField()
     mensaje_cifrado = models.TextField()
     fecha = models.DateTimeField(auto_now_add=True)

     #Metodo especial que define como se representara el objeto contacto como cadena
     def save(self, *args, **kwargs):
        #Cifrar el dato antes de guardarlo
        self.mensaje_cifrado = encrypt_message(self.mensaje)
        super().save(*args, **kwargs)

     def get_mensaje(self):
        #descifrar el mensaje al recuperarlo
        return decrypt_message(self.mensaje_cifrado)

     def __str__(self):
          #Devuelve el nombre del contacto como representacion en cadena del objeto
          return self.nombre     
