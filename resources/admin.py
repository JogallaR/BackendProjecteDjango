from django.contrib import admin
from .models import Recurs, Tag, Autor


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


class RecursAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["titol", "descripcio", "autor"]}),
        ("Extra", {"fields": ["categoria", "data_publicacio", "is_active"]}),
    ]
    inlines = [TagInline]


admin.site.register(Recurs, RecursAdmin)
admin.site.register(Autor)
admin.site.register(Tag)