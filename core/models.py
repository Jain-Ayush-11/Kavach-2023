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
    profile_summary = models.TextField(default="", blank=True, null=True)
    scam_reports = models.URLField(blank=True, null=True)

class Transaction(models.Model):
    transactionHash = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    logo = models.URLField(blank=True, null=True)
    sender = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=20, blank=True, null=True)
    reciever_to = models.CharField(max_length=34, blank=True, null=True)
    reciever_amount = models.CharField(max_length=20, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    wallets = models.CharField(blank=True, null=True, max_length=500)
    mixed_transaction = models.BooleanField(default=False)
    scam_reports = models.URLField(blank=True, null=True)

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

class Report(models.Model):
    address = models.CharField(max_length=512)
    coin = models.CharField(max_length=255)
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    information = models.TextField()

