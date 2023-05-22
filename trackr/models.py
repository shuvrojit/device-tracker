from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    pass


class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("-name",)
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ("-name",)
        verbose_name_plural = "Employees"


    def __str__(self):
        return self.name


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("-name",)
        verbose_name_plural = "Devices"


    def __str__(self):
        return self.name



class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(null=True, blank=True)
    condition = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.device} - {self.employee}"
