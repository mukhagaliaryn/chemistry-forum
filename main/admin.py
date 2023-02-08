from django.contrib import admin
from .models import Human


class HumanAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', )


admin.site.register(Human, HumanAdmin)
