from django.contrib import admin
from .models import Recurs, Tag

# Inline de Tag dins Recurs
class TagInline(admin.TabularInline):
    model = Tag
    extra = 1  # una línia extra buida per defecte

# Admin de Recurs personalitzat
class RecursAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["titol", "descripcio"]}),
        ("Més informació", {"fields": ["categoria", "data_publicacio", "is_active"], "classes": ["collapse"]}),
    ]
    inlines = [TagInline]
    list_display = ('titol', 'categoria', 'is_active', 'data_publicacio')
    list_filter = ('categoria', 'is_active')
    search_fields = ['titol', 'descripcio']

# Registrar al admin
admin.site.register(Recurs, RecursAdmin)