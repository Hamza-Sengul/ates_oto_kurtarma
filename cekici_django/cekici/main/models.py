from django.db import models

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    caption = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return self.caption if self.caption else f"Resim {self.id}"

class SiteContent(models.Model):
    about_us = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Site Content"
