from django.contrib import admin
from posts.models import Post, Comment, Profile
from tinymce.models import HTMLField

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)


class AdminEditor(admin.ModelAdmin):
    class Media:
        content = HTMLField()
