from django.contrib import admin
from .models import visitorLog, Comments, songRequest
# Register your models here.

@admin.register(visitorLog)
class visitorLogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comments)
admin.site.register(songRequest)
