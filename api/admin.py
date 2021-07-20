from django.contrib import admin

from api.models import (Category, Comment, CustomUser, EmailAndCode, Genre,
                        Review, Title)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'year',
        'description',
        'category',
    )
    search_fields = ('name',)


class EmailAndCodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'confirm_code', 'expire_date')


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'role')
    fieldsets = (
        (None, {'fields': (
            'first_name', 'last_name', 'email', 'username', 'bio', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )


admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(EmailAndCode, EmailAndCodeAdmin)
admin.site.register(CustomUser, UserAdmin)
