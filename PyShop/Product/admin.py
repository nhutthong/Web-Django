from django.contrib import admin
from .models import SanPham, Offer, Infomation

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class InformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'cls', 'major', 'school', 'score')

admin.site.register(Offer, OfferAdmin)
admin.site.register(SanPham, SanPhamAdmin)
admin.site.register(Infomation, InformationAdmin)
