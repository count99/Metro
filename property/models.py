from django.db import models

# Create your models here.


class Apart(models.Model):
    apart_name = models.CharField(verbose_name="股名", max_length=20)
    note = models.TextField(verbose_name="備註", blank=True, null=True)

    def __str__(self):
        return self.apart_name

    class Meta:
        verbose_name = '部門管理'
        verbose_name_plural = verbose_name


class Employee(models.Model):
    employee_number = models.CharField(verbose_name="員工編號", max_length=20)
    employee_name = models.CharField(verbose_name="姓名", max_length=20)
    apart = models.ForeignKey(Apart, verbose_name="所屬部門", on_delete=models.CASCADE)
    password = models.CharField(verbose_name="密碼", max_length=50)
    note = models.TextField(verbose_name="備註", blank=True, null=True)

    def __str__(self):
        return self.employee_name

    class Meta:
        verbose_name = '員工管理'
        verbose_name_plural = verbose_name


class Station(models.Model):
    station_name = models.CharField(verbose_name="站名", max_length=20)
    apart = models.ForeignKey(Apart, verbose_name="所屬部門", on_delete=models.CASCADE)
    station_number = models.CharField(verbose_name="車站編號", max_length=20)
    station_ip_1 = models.CharField(verbose_name="通訊所屬ip網段1", max_length=20)
    station_ip_2 = models.CharField(verbose_name="通訊所屬ip網段2", max_length=20)
    station_ip_3 = models.CharField(verbose_name="資訊所屬ip網段1", max_length=20)
    note = models.TextField(verbose_name="備註", blank=True, null=True)

    def __str__(self):
        return self.station_name

    class Meta:
        verbose_name = '捷運站管理'
        verbose_name_plural = verbose_name


class Product(models.Model):
    product_name = models.CharField(verbose_name="設備", max_length=20)
    company_name = models.CharField(verbose_name="廠牌名", max_length=20)
    product_type = models.CharField(verbose_name="類型", max_length=20)
    product_account = models.CharField(verbose_name="產品預設帳號", max_length=20, blank=True, null=True)
    product_password = models.CharField(verbose_name="產品預設密碼", max_length=20, blank=True, null=True)
    note = models.TextField(verbose_name="備註", blank=True, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = '設備型號管理'
        verbose_name_plural = verbose_name


class Equipment(models.Model):
    equipment_name = models.CharField(verbose_name="設備名稱", max_length=50)
    station = models.ForeignKey(Station, verbose_name="所屬車站", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="設備型號", on_delete=models.CASCADE)
    ip = models.CharField(verbose_name="設備ip", max_length=20)
    status = models.CharField(verbose_name="設備狀態", max_length=20)
    setup_time = models.DateField(verbose_name="安裝日期", auto_now_add=True)
    note = models.TextField(verbose_name="備註", blank=True, null=True)

    def __str__(self):
        return self.equipment_name

    class Meta:
        verbose_name = '設備設定管理'
        verbose_name_plural = verbose_name
