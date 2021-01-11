from django.contrib import admin

from .models import Show, Spent


# Register your models here.
class ShowAdmin(admin.ModelAdmin):
    list_display = ('show',)
    # prepopulated_fields = {'slug': ('show',)}


admin.site.register(Show, ShowAdmin)
admin.site.register(Spent)
