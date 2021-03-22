from django.db import models


class Lead(models.Model):
    
    SOURCE_CHOICES = (
        ("YouTube", "YouTube"),
        ("Google", "Google"),
        ("Newsletter", "Newsletter"),
    )
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    
    phoned = models.BooleanField(default=False)
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    
    profile_picture = models.ImageField(blank=True, null=True)
    special_fields = models.FileField(blank=True, null=True)