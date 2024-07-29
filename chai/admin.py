from django.contrib import admin
from .models import chaiVarity,ChaiReview,ChaiCertificate,Store

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model=ChaiReview
    extra=2


class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')    
    inlines=[ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varities',) 

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')       




admin.site.register(chaiVarity,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)

admin.site.register(ChaiCertificate,ChaiCertificateAdmin)

