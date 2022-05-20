from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sostav', 'ves', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'sostav')
    actions = ["publish", "unpublish"]


admin.site.register(Food, FoodAdmin)
admin.site.register(Work)
admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(Actions)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Forum)
admin.site.register(New)
admin.site.register(About)


def unpublish(self, request, queryset):
    row_update = queryset.update(draft=True)
    if row_update == 1:
        message_bit = "1 запись была обновлена"
    else:
        message_bit = f"{row_update} записей были обновлены"
    self.message_user(request, f"{message_bit}")


def publish(self, request, queryset):
    row_update = queryset.update(draft=False)
    if row_update == 1:
        message_bit = "1 запись была обновлена"
    else:
        message_bit = f"{row_update} записей были обновлены"
    self.message_user(request, f"{message_bit}")


publish.short_description = "Опубликовать"
publish.allowed_permission = ('change', )

unpublish.short_description = "Снять с публикации"
unpublish.allowed_permission = ('change', )