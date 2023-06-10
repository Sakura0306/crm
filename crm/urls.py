from django.urls import path
from . import views

urlpatterns = [
    path('', views.company, name='company'),
    path('company/', views.company, name='company'),
    path('company/<int:company_id>', views.company_delete, name='company_delete'),
    path('company/edit/<int:company_id>', views.company_edit, name='company_edit'),

    path('employee/', views.employee, name='employee'),
    path('employee/<int:employee_id>', views.employee_delete, name='employee_delete'),
    path('employee/edit/<int:employee_id>', views.employee_edit, name='employee_edit'),

    path('deal/', views.deal, name='deal'),
    path('deal/<int:deal_id>', views.deal_delete, name='deal_delete'),
    path('deal/edit/<int:deal_id>', views.deal_edit, name='deal_edit'),

    path('note/', views.note, name='note'),
    path('note/<int:note_id>', views.note_delete, name='note_delete'),
    path('note/edit/<int:note_id>', views.note_edit, name='note_edit'),

    path('meeting/', views.meeting, name='meeting'),
    path('meeting/<int:meeting_id>', views.meeting_delete, name='meeting_delete'),
    path('meeting/edit/<int:meeting_id>', views.meeting_edit, name='meeting_edit'),
]