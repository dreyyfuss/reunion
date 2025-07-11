from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Photo, Comment

User = get_user_model()

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('user', 'created_at', 'short_text')
    fields = ('user', 'short_text', 'created_at')
    can_delete = True
    
    def short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Comment'

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'user', 'uploaded_at', 'comment_count')
    list_filter = ('uploaded_at', 'user')
    search_fields = ('caption', 'user__email')
    readonly_fields = ('uploaded_at', 'thumbnail')
    fieldsets = (
        (None, {
            'fields': ('user', 'image', 'caption')
        }),
        ('Metadata', {
            'fields': ('uploaded_at', 'thumbnail'),
            'classes': ('collapse',)
        }),
    )
    inlines = [CommentInline]
    
    def thumbnail(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "-"
    thumbnail.short_description = 'Preview'
    
    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = 'Comments'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo_thumbnail', 'short_text', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('text', 'photo__caption', 'user__email')
    readonly_fields = ('created_at', 'photo_thumbnail')
    fields = ('user', 'photo', 'photo_thumbnail', 'text', 'created_at')
    
    def short_text(self, obj):
        return obj.text[:75] + '...' if len(obj.text) > 75 else obj.text
    short_text.short_description = 'Comment'
    
    def photo_thumbnail(self, obj):
        from django.utils.html import format_html
        if obj.photo.image:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="50" height="50" style="object-fit: cover;" /></a>',
                obj.photo.get_absolute_url(),
                obj.photo.image.url
            )
        return "-"
    photo_thumbnail.short_description = 'Photo'