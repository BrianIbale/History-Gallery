from django.contrib import admin
from .models import Person, PersonDetail

# Register your models here.
admin.site.register(Person)
admin.site.register(PersonDetail)