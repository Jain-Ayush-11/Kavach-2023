from django.contrib import admin
from . import models

class CustomModelAdmin(admin.ModelAdmin):
    
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(CustomModelAdmin, self).__init__(model, admin_site)

class SocialMediaAdmin(CustomModelAdmin):
    pass

class TransactionAdmin(CustomModelAdmin):
    pass

class WatchlistAdmin(CustomModelAdmin):
    pass

class WebsiteReportAdmin(CustomModelAdmin):
    pass

admin.site.register(models.SocialMedia, SocialMediaAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
admin.site.register(models.Watchlist, WatchlistAdmin)
admin.site.register(models.WebsiteReport, WebsiteReportAdmin)
admin.site.register(models.Report)