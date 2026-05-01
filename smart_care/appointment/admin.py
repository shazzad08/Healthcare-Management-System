from django.contrib import admin
from .import models
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name','doctor_name','appointment_types','appointment_status','symptom','time','cancel']


    def patient_name(self,obj):
        return obj.patient.user.first_name 

    def doctor_name(self,obj):
        return obj.doctor.user.last_name


admin.site.register(models.Appointment,AppointmentAdmin)
