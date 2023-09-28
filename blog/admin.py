from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'about',
        'price',
        'duration',
        'image',
        'phone',
    )

    list_display = ['title','about','price','duration','image','phone']
    


admin.site.register(Contact)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'title',
        'reading',
        'listening',
        'writing',
        'speaking',
    )     

    list_display = ['image', 'title', 'reading', 'listening', 'writing', 'speaking']


@admin.register(Vidoheader)
class VidioAdmin(admin.ModelAdmin):
    fields = (
        'vidio',
    )

    list_display = ['vidio']


