from django.contrib import admin

# Register your models here.
from kotlinApp.models import User, Product, Appointment, Member
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Member)