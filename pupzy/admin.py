from django.contrib import admin
from .models import Stuff
from .models import Contact
from .models import Orders, OrderUpdate


# Register your models here.
admin.site.register(Stuff)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)