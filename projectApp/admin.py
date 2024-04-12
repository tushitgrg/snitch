from django.contrib import admin
from .models import Topics
from .models import snitch
from .models import Message, imageuser

admin.site.register(Topics)
admin.site.register(snitch)
admin.site.register(Message)
admin.site.register(imageuser)
# Register your models here.
