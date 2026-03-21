from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProductSet

@admin.register(ProductSet)
class ProductSetAdmin(admin.ModelAdmin):
    # Тизмеде көрүнө турган маалыматтар
    list_display = ('get_image', 'title', 'pieces', 'price', 'ready_time')
    list_display_links = ('title',) # Атын басканда ичине кирет

    # Сүрөттү кичинекей кылып көрсөтүү
    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60" height="60" style="border-radius:8px; object-fit:cover;">')
        return "Сүрөт жок"
    
    get_image.short_description = "Сүрөтү"