from django.contrib import admin

from .models import Advertisment
# Register your models here.

class Advertismentadmin(admin.ModelAdmin):
    list_display = ['title','descriptions','price','trades','date_now',"created_date"]
    list_filter = ['date_now','descriptions','trades']
    fieldsets = (
        ("Первый блок",{
            "fields":("title","descriptions")}),
        ("Второй блок",{
            'classes': ('collapse',),
            "fields":('price','trades')}),
        )
    actions = ['make_true','make_False','created_date']
    @admin.action(description="Обновить торг на True")
    def make_true(self,request,queryset):
        queryset.update(trades = True)

    @admin.action(description="Обновить торг на False")
    def make_False(self, request, queryset):
        queryset.update(trades=False)


admin.site.register(Advertisment,Advertismentadmin)

