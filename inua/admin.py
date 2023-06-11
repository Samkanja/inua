from django.contrib import admin

from .models import Activity,Program,AboutUs

# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title',)}



admin.site.register(AboutUs)
