from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    ingredientes = models.TextField()

    def __str__(self):
        return self.name
    

# python manage.py makemigrations <------- lee el arhivo models y crea una arhcivo de migracion
# python manage.py migrate <-------- tomar las migraciones pendientes y volcarlas contra la BBDD (sql)
# python manage.yp createsuperuser

#template -----> view -----> url


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_email
    
# class MyModelName(models.Model):
#     """
#     Una clase típica definiendo un modelo, derivado desde la clase Model.
#     """

#     # Campos
#     my_field_name = models.CharField(max_lenght=20, help_text="Enter field documentaion")

#     # Metadata
#     class Meta:
#         ordering = ["-my_field_name"]

#     def get_absolute_url(self):
#         """
#         Devuelve la url para acceder a una instancia particular de MyModelName
#         """
#         return reverse('model-detail-view', args=[str(self.id)])
    
#     def __str__(self):
#         """
#         Cadena para representar el objeto MyModelName(en el sitio Admin, etc.)
#         """
#         return self.field_name