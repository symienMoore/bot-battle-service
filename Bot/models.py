from django.db import models

# Create your models here.
class Robot(models.Model):
    name           = models.CharField(max_length=255)
    special_attack = models.CharField(max_length=255)
    type           = models.CharField(max_length=255)
    created_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
   


        