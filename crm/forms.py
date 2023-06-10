from django import forms
from django.forms import ModelChoiceField

from crm.models import Employee, Deal, Company


class ModelChoiceFieldNameDisplay(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class CompanyForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    business_field = forms.CharField(max_length=255)


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=255)
    wid = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    position = forms.CharField(max_length=255)
    company = ModelChoiceFieldNameDisplay(queryset=Company.objects.all())


class DealForm(forms.Form):
    name = forms.CharField(max_length=255)
    budget = forms.IntegerField()
    currency = forms.CharField(max_length=255)
    status = forms.CharField(max_length=255)
    company = ModelChoiceFieldNameDisplay(queryset=Company.objects.all())
    contact_point = ModelChoiceFieldNameDisplay(queryset=Employee.objects.all())


class NoteForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    deal = ModelChoiceFieldNameDisplay(queryset=Deal.objects.all())


class MeetingForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    organizer = ModelChoiceFieldNameDisplay(queryset=Employee.objects.all())
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    deal = ModelChoiceFieldNameDisplay(queryset=Deal.objects.all())
