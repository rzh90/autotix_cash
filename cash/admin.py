from django.contrib import admin

from .models import Show, Spent


# Register your models here.
class ShowAdmin(admin.ModelAdmin):
    list_display = ('show', 'slug', 'date_added')
    # prepopulated_fields = {'slug': ('show',)}


class SpentAdmin(admin.ModelAdmin):
    list_display = ('date_added', 'amount', 'show')


admin.site.register(Show, ShowAdmin)
admin.site.register(Spent, SpentAdmin)
