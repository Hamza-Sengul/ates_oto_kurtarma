from django.shortcuts import render
from .models import SliderImage, SiteContent

def index(request):
    slider_images = SliderImage.objects.all()
    site_content = SiteContent.objects.first()
    return render(request, 'index.html', {'slider_images': slider_images, 'site_content': site_content})
