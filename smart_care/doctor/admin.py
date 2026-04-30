from django.contrib import admin
from  .import models

# Register your models here.
class specializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
class designationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class DoctorAdmin (admin.ModelAdmin):
    list_display = ('name', 'fees')

    def name(self, obj):
        return obj.user.get_full_name()



admin.site.register(models.AvailableTime)
admin.site.register(models.Specialization,specializationAdmin)
admin.site.register(models.Designation,designationAdmin)
admin.site.register(models.Doctor,DoctorAdmin)



