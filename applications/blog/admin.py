from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.blog.models import NewsImage, New


class InlineNewsImage(admin.TabularInline):
    model = NewsImage
    extra = 1
    fields = ['image', ]


class DisplayAdminNews(admin.ModelAdmin):
    inlines = [InlineNewsImage, ]

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain" />')
        else:
            return ""


admin.site.register(New, DisplayAdminNews)
