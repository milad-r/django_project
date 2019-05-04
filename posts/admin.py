from django.contrib import admin
from . import models



@admin.register(models.Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('first_name' , 'last_name' , 'birthDay')
    fields = ['first_name' , 'last_name' , 'birthDay' ]

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title' , 'body' , 'timestamp' , 'writer' , 'assortment' ]
    list_display = ('title' , 'timestamp')

@admin.register(models.Assortment)
class assortmentAdmin(admin.ModelAdmin):
    fields = ['name']    