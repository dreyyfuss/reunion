from django.contrib import admin
from .models import DepartedMember, Tribute

@admin.register(DepartedMember)
class DepartedMemberAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tribute)
class TributeAdmin(admin.ModelAdmin):
    list_display = ('author', 'departed', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__email', 'departed__name')