from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

# @admin.register(Post): This is a decorator used in Django's admin to register the
# "Post" model with the admin interface. It means that the "Post" model can now be
# managed and edited through the Django admin panel.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    # summernote_fields = ('content'): This line specifies that the "content" field of the "Post"
    # model should use the Summernote editor in the admin interface. The summernote_fields attribute
    # is a tuple that contains the names of fields you want to enhance with the Summernote editor.
    # In this case, it's just the "content" field.
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments',]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# admin.site.register(Post)
