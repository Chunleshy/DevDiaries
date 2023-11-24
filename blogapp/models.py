from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    # publish = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"pk":self.pk, "slug": self.slug})  