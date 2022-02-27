from django.contrib import admin
from contact.forms import ContactForm

from contact.models import *

# Register your models here.
admin.site.register(Contact)