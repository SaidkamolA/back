from django.contrib import admin

from gul.models import Order
from users.models import User, VerificationCode

# Register your models here.
admin.site.register(Order)

admin.site.register(User)
admin.site.register(VerificationCode)