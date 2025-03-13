from django.db import models
from django.urls import reverse

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=100)    
    body = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('publication-detail', kwargs={'pk': self.pk})