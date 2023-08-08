from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    logo = models.FileField(null=True, blank=True)
    social_media = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    latest_post_date = models.DateField(null=True, blank=True)
    account_rating = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    account_reached = models.BigIntegerField(null=True, blank=True)
    engagement = models.BigIntegerField(null=True, blank=True)
    views = models.BigIntegerField(null=True, blank=True)
    profile_visited = models.BigIntegerField(null=True, blank=True)

