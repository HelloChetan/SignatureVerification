from django.contrib import admin

# Register your models here.
from Main.models import CustomerDetail
from Main.models import VerificationDetail
from Main.models import Attachment

admin.site.register(CustomerDetail)
admin.site.register(VerificationDetail)
admin.site.register(Attachment)