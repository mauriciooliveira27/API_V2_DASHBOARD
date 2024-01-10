

from django.contrib import admin
from .models import DashBoard




# Register your models here.
@admin.register(DashBoard)
class DashBoardAdmin(admin.ModelAdmin):
    list_display = ('create' , 'update') 