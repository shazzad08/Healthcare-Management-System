from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name= models.CharField(max_length=20)
    phone= models.CharField(max_length=12)
    problem= models.TextField()
    
    def __str__(self):  #object কে readable text হিসেবে দেখানোর জন্য
          return self.name   # Example: "Rahim" দেখাবে, object (1) না
    
    class Meta:                  # model এর plural (বহুবচন) নাম সেট করার জন্য
            verbose_name_plural = "Contact Us"  