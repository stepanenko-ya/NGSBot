from django.contrib import admin
from. models import Message, Activities, Admins, ClientAdmin


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    pass


@admin.register(Admins)
class AdminsAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientAdmin)
class ClientAdminAdmin(admin.ModelAdmin):
    pass
