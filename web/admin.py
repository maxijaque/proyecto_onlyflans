from django.contrib import admin
from .models import Flan, ContactForm

class FlansAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    # list_filter = genero
    # list_per_page = 1, 2, 10
# Register your models here.
admin.site.register(Flan, FlansAdmin)
admin.site.register(ContactForm)
