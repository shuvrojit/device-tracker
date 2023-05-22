from django.contrib import admin

from .models import Company, Employee, Device, DeviceLog

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)

@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):

    list_display = ("device", "employee", "checkout_time", "return_time", "condition")
    list_filter = ("device", "employee", "checkout_time", "return_time", "condition")
    list_editable = ("return_time", "condition")
