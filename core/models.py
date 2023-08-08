from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    address = models.CharField(max_length=512, blank=True, null=True)
    logo = models.URLField(null=True, blank=True)
    social_media = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    latest_post_date = models.DateField(null=True, blank=True)
    account_rating = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    account_reached = models.BigIntegerField(null=True, blank=True)
    engagement = models.BigIntegerField(null=True, blank=True)
    views = models.BigIntegerField(null=True, blank=True)
    profile_visited = models.BigIntegerField(null=True, blank=True)
    risk = models.CharField(max_length=255, default="High")
    profile_summary = models.TextField(default="")

class Transaction(models.Model):
    address = models.CharField(max_length=512, unique=True)
    type_of_event = models.CharField(max_length=255, null=True, blank=True)
    sender_address = models.CharField(max_length=512, null=True, blank=True)
    recipient_address = models.CharField(max_length=255, null=True, blank=True)
    time_of_transaction = models.DateTimeField(null=True, blank=True)
    previous_report = models.CharField(max_length=255, null=True, blank=True)
    block_height = models.CharField(max_length=255, null=True, blank=True)
    type_of_blockchain = models.CharField(max_length=255, null=True, blank=True)

class Watchlist(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, unique=True)
    coin = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    notify = models.CharField(max_length=255, null=True, blank=True)
    email_template = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

class WebsiteReport(models.Model):
    url = models.URLField(unique=True, blank=True, null=True)
    report_id = models.CharField(blank=True, null=True, max_length=500)
