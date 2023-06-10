from django.shortcuts import render, redirect

from .forms import CompanyForm, EmployeeForm, DealForm, NoteForm, MeetingForm
from .models import Company, Employee, Deal, Note, Meeting


# Create your views here.
def company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        Company.objects.create(name=form.data['name'], email=form.data['email'],
                               phone_number=form.data['phone_number'], address=form.data['address'],
                               business_field=form.data['business_field'])
        return redirect('/company')
    context = {'companies': Company.objects.all(),
               'form': CompanyForm()}
    return render(request, 'company/list.html', context)


def company_delete(request, company_id):
    Company.objects.filter(id=company_id).delete()
    return redirect('/company')


def company_edit(request, company_id):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        Company.objects.filter(id=company_id).update(name=form.data['name'], email=form.data['email'],
                                                     phone_number=form.data['phone_number'],
                                                     address=form.data['address'],
                                                     business_field=form.data['business_field'])
        return redirect('/company')
    context = {'company': Company.objects.get(id=company_id),
               'form': CompanyForm(request.POST or None, initial=Company.objects.get(id=company_id).__dict__)}
    return render(request, 'company/edit.html', context)



def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        Employee.objects.create(name=form.data['name'], wid=form.data['wid'], email=form.data['email'],
                                phone_number=form.data['phone_number'], address=form.data['address'],
                                position=form.data['position'], company_id=form.data['company'])
        return redirect('/employee')
    context = {'employees': Employee.objects.all(),
               'companies': Company.objects.all(),
               'form': EmployeeForm()}
    return render(request, 'employee/list.html', context)


def employee_delete(request, employee_id):
    Employee.objects.filter(id=employee_id).delete()
    return redirect('/employee')


def employee_edit(request, employee_id):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        Employee.objects.filter(id=employee_id).update(name=form.data['name'], wid=form.data['wid'],
                                                       email=form.data['email'],
                                                       phone_number=form.data['phone_number'],
                                                       address=form.data['address'],
                                                       position=form.data['position'],
                                                       company_id=form.data['company'])
        return redirect('/employee')
    context = {'employee': Employee.objects.get(id=employee_id),
               'companies': Company.objects.all(),
               'form': EmployeeForm(request.POST or None, initial=Employee.objects.get(id=employee_id).__dict__)}
    return render(request, 'employee/edit.html', context)



def deal(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        Deal.objects.create(name=form.data['name'], budget=form.data['budget'], currency=form.data['currency'],
                            status=form.data['status'], company_id=form.data['company'],
                            employee_id=form.data['contact_point'])
        return redirect('/deal')
    context = {'deals': Deal.objects.all(),
               'companies': Company.objects.all(),
               'employees': Employee.objects.all(),
               'form': DealForm()}
    return render(request, 'deal/list.html', context)


def deal_delete(request, deal_id):
    Deal.objects.filter(id=deal_id).delete()
    return redirect('/deal')


def deal_edit(request, deal_id):
    if request.method == 'POST':
        form = DealForm(request.POST)
        Deal.objects.filter(id=deal_id).update(name=form.data['name'], budget=form.data['budget'],
                                               currency=form.data['currency'], status=form.data['status'],
                                               company_id=form.data['company'],
                                               employee_id=form.data['contact_point'])
        return redirect('/deal')
    context = {'deal': Deal.objects.get(id=deal_id),
               'companies': Company.objects.all(),
               'employees': Employee.objects.all(),
               'form': DealForm(request.POST or None, initial=Deal.objects.get(id=deal_id).__dict__)}
    return render(request, 'deal/edit.html', context)



def note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        Note.objects.create(title=form.data['title'], description=form.data['description'],
                            deal_id=form.data['deal'])
        return redirect('/note')
    context = {'notes': Note.objects.all(),
               'deals': Deal.objects.all(),
               'form': NoteForm()}
    return render(request, 'note/list.html', context)


def note_delete(request, note_id):
    Note.objects.filter(id=note_id).delete()
    return redirect('/note')


def note_edit(request, note_id):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        Note.objects.filter(id=note_id).update(title=form.data['title'], description=form.data['description'],
                                               deal=form.data['deal'])
        return redirect('/note')
    context = {'note': Note.objects.get(id=note_id),
               'deals': Deal.objects.all(),
               'form': NoteForm(request.POST or None, initial=Note.objects.get(id=note_id).__dict__)}
    return render(request, 'note/edit.html', context)


def meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        Meeting.objects.create(title=form.data['title'], description=form.data['description'],
                               organizer_id=form.data['organizer'], date=form.data['date'],
                               deal_id=form.data['deal'])
        return redirect('/meeting')
    context = {'meetings': Meeting.objects.all(),
               'employees': Employee.objects.all(),
               'deals': Deal.objects.all(),
               'form': MeetingForm()}
    return render(request, 'meeting/list.html', context)


def meeting_delete(request, meeting_id):
    Meeting.objects.filter(id=meeting_id).delete()
    return redirect('/meeting')


def meeting_edit(request, meeting_id):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        Meeting.objects.filter(id=meeting_id).update(title=form.data['title'], description=form.data['description'],
                                                     organizer=form.data['organizer'], date=form.data['date'],
                                                     deal=form.data['deal'])
        return redirect('/meeting')
    context = {'meeting': Meeting.objects.get(id=meeting_id),
               'employees': Employee.objects.all(),
               'deals': Deal.objects.all(),
               'form': MeetingForm(request.POST or None, initial=Meeting.objects.get(id=meeting_id).__dict__)}
    return render(request, 'meeting/edit.html', context)
