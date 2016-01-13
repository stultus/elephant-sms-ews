from django.contrib import admin
from .models import Informer,Subscriber,Siting,Message

# Register your models here.
admin.site.register(Siting)
admin.site.register(Informer)
admin.site.register(Subscriber)
admin.site.register(Message)
