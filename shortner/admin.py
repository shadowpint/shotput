from django.contrib import admin

from shortner.models import *


@admin.register(ShortUrlModel)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_id', 'url', 'created_at', 'count')
    list_filter = ('created_at',)
