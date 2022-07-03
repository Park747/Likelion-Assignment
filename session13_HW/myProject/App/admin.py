from django.contrib import admin
from .models import visitorLog, Comments, songRequest, User, Like
# Register your models here.

@admin.register(visitorLog)
class visitorLogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comments)
admin.site.register(songRequest)
admin.site.register(Like)

