from django.contrib import admin
from nextcloudappstore.core.models import DatabaseDependency, AppRelease, \
    ShellCommand, Screenshot, PhpExtensionDependency, License, PhpExtension, \
    Database, AppRating, App, Category, AppAuthor, AppOwnershipTransfer

from parler.admin import TranslatableAdmin


class DatabaseDependencyInline(admin.TabularInline):
    model = DatabaseDependency
    extra = 1


class PhpExtensionDependencyInline(admin.TabularInline):
    model = PhpExtensionDependency
    extra = 1


@admin.register(AppRelease)
class AppReleaseAdmin(TranslatableAdmin):
    inlines = (DatabaseDependencyInline, PhpExtensionDependencyInline)
    list_filter = ('last_modified', 'app__owner', 'app__id')
    ordering = ('-last_modified',)


@admin.register(AppAuthor)
class AppAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'homepage')


@admin.register(AppOwnershipTransfer)
class AppOwnershipTransferAdmin(admin.ModelAdmin):
    list_display = ('app', 'from_user', 'to_user', 'proposed')
    list_filter = ('app', 'from_user', 'to_user', 'proposed')


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('id', 'name')


@admin.register(App)
class AppAdmin(TranslatableAdmin):
    list_display = ('id', 'owner', 'name', 'last_release', 'rating_recent',
                    'rating_overall', 'summary', 'ocsid')
    list_filter = ('owner', 'co_maintainers', 'categories', 'created',
                   'last_release')
    ordering = ('id',)


@admin.register(AppRating)
class AppRatingAdmin(TranslatableAdmin):
    list_display = ('rating', 'app', 'user', 'rated_at')
    list_filter = ('app__id', 'user', 'rating', 'rated_at')


@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(DatabaseDependency)
class DatabaseDependencyAdmin(admin.ModelAdmin):
    list_display = ('app_release', 'database', 'version_spec')
    list_filter = ('app_release', 'database')


@admin.register(PhpExtension)
class PhpExtensionAdmin(admin.ModelAdmin):
    pass


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(PhpExtensionDependency)
class PhpExtensionDependencyAdmin(admin.ModelAdmin):
    list_display = ('app_release', 'php_extension', 'version_spec')
    list_filter = ('app_release', 'php_extension')


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    ordering = ('app', 'ordering')
    list_display = ('url', 'app', 'ordering')
    list_filter = ('app__id',)


@admin.register(ShellCommand)
class ShellCommandAdmin(admin.ModelAdmin):
    pass
