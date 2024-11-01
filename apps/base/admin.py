from django.contrib import admin
from .models import Todo_list

# Register your models here.

@admin.register(Todo_list)
class Todo_listAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'is_completed', 'created']