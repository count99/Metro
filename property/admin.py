from django.contrib import admin
from .models import Apart, Employee, Station, Product, Equipment
# Register your models here.

admin.site.site_header = "通訊設備管理介面"
admin.site.register(Apart)
admin.site.register(Employee)
admin.site.register(Station)
admin.site.register(Product)
admin.site.register(Equipment)
