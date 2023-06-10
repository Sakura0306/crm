from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    business_field = models.CharField(max_length=255)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    wid = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)


class Deal(models.Model):
    name = models.CharField(max_length=255)
    budget = models.IntegerField()
    currency = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)


class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    deal = models.ForeignKey(Deal, on_delete=models.DO_NOTHING)


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    organizer = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    deal = models.ForeignKey(Deal, on_delete=models.DO_NOTHING)
