from django.contrib import admin

from .models import AutoProject,Comment
# Register your models here.
admin.site.register(AutoProject)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
#
# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)
#
# admin.site.register(Post, PostAdmin)
