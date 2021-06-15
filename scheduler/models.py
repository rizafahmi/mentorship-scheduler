from django.db import models

# Create your models here.
class Mentor(models.Model):
    name = models.CharField(max_length=100, help_text="Masukkan nama mentor")
    email = models.EmailField(max_length=125, help_text="Masukkan email mentor")
    price = models.IntegerField(help_text="Masukkan biaya per menit")

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
        
