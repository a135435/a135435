from django.contrib import admin
from .models import Direction, Research, Member


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'direction', 'publish_date', 'is_featured')
    list_filter = ('direction', 'publish_date', 'is_featured')
    search_fields = ('title', 'content', 'summary')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_key_member', 'order')
    list_filter = ('is_key_member', 'position')
    search_fields = ('name', 'position', 'bio')
    ordering = ('order', 'name')