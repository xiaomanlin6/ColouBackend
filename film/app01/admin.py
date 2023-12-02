from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from app01.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UserInfoAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email", "gender", "avatar", "company", "digg_film")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "name", "gender", "company")

    list_filter = ("is_superuser", "is_active")

    search_fields = ("username", "name", "userinfo")


class CourseResources(resources.ModelResource):
    class Meta:
        model = Color
        exclude = ['nid', 'create_time']
        import_id_fields = ['title']


class ColorAdmin(ImportExportModelAdmin):
    def get_username(self):
        if not self.user:
            return 'None'
        return self.user.username

    get_username.short_description = 'Publisher'

    list_display = ['title', get_username, 'content', 'comment_count', 'digg_count', 'create_time']

    list_filter = ['title', 'create_time']

    search_fields = ['user__username', 'user__name']

    resource_class = CourseResources


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'create_time']

    list_filter = ['create_time']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Sharing)
admin.site.register(Collect)
admin.site.register(CommentSharing)
admin.site.register(FeedBack)

