from django.contrib import admin
from django.utils.html import format_html
from .models import Photo, Comment

class CommentInline(admin.TabularInline):
    """Inline admin interface for Comments"""
    model = Comment
    extra = 0
    readonly_fields = ('user', 'text', 'created_at')
    fields = ('user', 'text', 'created_at')
    can_delete = False
    
    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Admin interface for Photos"""
    list_display = ('thumbnail', 'user_email', 'caption_preview', 'upload_date', 'comment_count')
    list_filter = ('uploaded_at', 'user')
    search_fields = ('caption', 'user__email')
    readonly_fields = ('thumbnail_preview', 'uploaded_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'uploaded_at')
        }),
        ('Photo Content', {
            'fields': ('image', 'thumbnail_preview', 'caption')
        }),
    )
    inlines = [CommentInline]
    
    def user_email(self, obj):
        return obj.user.email if obj.user else 'Anonymous'
    user_email.short_description = 'Uploaded By'
    user_email.admin_order_field = 'user__email'
    
    def caption_preview(self, obj):
        return obj.caption[:50] + '...' if obj.caption else 'No caption'
    caption_preview.short_description = 'Caption Preview'
    
    def upload_date(self, obj):
        return obj.uploaded_at.strftime('%b %d, %Y')
    upload_date.short_description = 'Upload Date'
    upload_date.admin_order_field = 'uploaded_at'
    
    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.image.url
            )
        return '-'
    thumbnail.short_description = 'Thumbnail'
    
    def thumbnail_preview(self, obj):
        return self.thumbnail(obj)
    thumbnail_preview.short_description = 'Preview'
    
    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = 'Comments'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for Comments"""
    list_display = ('user_email', 'photo_thumbnail', 'text_preview', 'created_date')
    list_filter = ('created_at', 'user')
    search_fields = ('text', 'user__email', 'photo__caption')
    readonly_fields = ('created_at',)
    
    def user_email(self, obj):
        return obj.user.email if obj.user else 'Anonymous'
    user_email.short_description = 'Comment By'
    user_email.admin_order_field = 'user__email'
    
    def photo_thumbnail(self, obj):
        if obj.photo.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.photo.image.url
            )
        return '-'
    photo_thumbnail.short_description = 'Photo'
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if obj.text else 'No text'
    text_preview.short_description = 'Comment Preview'
    
    def created_date(self, obj):
        return obj.created_at.strftime('%b %d, %Y')
    created_date.short_description = 'Created Date'
    created_date.admin_order_field = 'created_at'

# Optional: Custom admin site header
admin.site.site_header = 'Gallery Administration'
admin.site.site_title = 'Gallery Admin Portal'
admin.site.index_title = 'Welcome to Gallery Admin'