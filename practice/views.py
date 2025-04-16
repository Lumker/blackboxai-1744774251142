from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client, Case, Document, Billing, Appointment

@login_required
def dashboard(request):
    cases = Case.objects.filter(assigned_attorney=request.user).order_by('-created_at')[:5]
    appointments = Appointment.objects.filter(attendees=request.user).order_by('date', 'start_time')[:5]
    context = {
        'cases': cases,
        'appointments': appointments,
    }
    return render(request, 'practice/dashboard.html', context)

@login_required
def client_list(request):
    clients = Client.objects.all().order_by('name')
    return render(request, 'practice/client_list.html', {'clients': clients})

@login_required
def case_list(request):
    cases = Case.objects.all().order_by('-created_at')
    return render(request, 'practice/case_list.html', {'cases': cases})

@login_required
def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    documents = case.documents.all()
    appointments = case.appointments.all()
    billings = case.billings.all()
    context = {
        'case': case,
        'documents': documents,
        'appointments': appointments,
        'billings': billings,
    }
    return render(request, 'practice/case_detail.html', context)

@login_required
def appointment_calendar(request):
    appointments = Appointment.objects.all().order_by('date', 'start_time')
    return render(request, 'practice/appointment_calendar.html', {'appointments': appointments})

@login_required
def billing_list(request):
    billings = Billing.objects.all().order_by('-due_date')
    return render(request, 'practice/billing_list.html', {'billings': billings})
