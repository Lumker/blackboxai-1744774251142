from django.contrib import admin
from .models import Client, Case, Document, Billing, Appointment

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'registration_date')
    search_fields = ('name', 'email')
    list_filter = ('registration_date',)

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'status', 'start_date', 'assigned_attorney')
    list_filter = ('status', 'start_date', 'assigned_attorney')
    search_fields = ('title', 'client__name', 'description')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'case', 'uploaded_by', 'uploaded_at')
    list_filter = ('uploaded_at', 'uploaded_by')
    search_fields = ('title', 'case__title')

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('case', 'amount', 'status', 'due_date')
    list_filter = ('status', 'due_date')
    search_fields = ('case__title', 'description')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'case', 'date', 'start_time', 'end_time')
    list_filter = ('date', 'created_at')
    search_fields = ('title', 'case__title', 'description')
