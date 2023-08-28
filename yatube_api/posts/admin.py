from django.contrib import admin

from posts.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    model = Group
    fields = ('title', 'slug', 'description',)
