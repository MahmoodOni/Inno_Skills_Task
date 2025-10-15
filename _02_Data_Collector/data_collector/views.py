from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SimpleRecord

def simple_form(request):
    """Handle the form display and submission"""
    
    if request.method == 'POST':
        # Get data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        uploaded_file = request.FILES.get('file')
        
        # Calculate sizes (simple method)
        name_size = len(name) / 1024  # Rough estimate in KB
        email_size = len(email) / 1024
        phone_size = len(phone) / 1024
        file_size = uploaded_file.size / 1024 if uploaded_file else 0
        total_size = name_size + email_size + phone_size + file_size
        
        # Save to database
        record = SimpleRecord(
            name=name,
            email=email,
            phone=phone,
            file=uploaded_file,
            name_size=name_size,
            email_size=email_size,
            phone_size=phone_size,
            file_size=file_size,
            total_size=total_size
        )
        record.save()
        
        # Show success page
        return render(request, 'success.html', {
            'record': record
        })
    
    # If GET request, just show the form
    return render(request, 'simple_form.html')

def show_all_data(request):
    """Show all records in a table with totals"""
    records = SimpleRecord.objects.all().order_by('-created_at')
    
    # Calculate totals for the footer row
    total_name_size = sum(record.name_size for record in records)
    total_email_size = sum(record.email_size for record in records)
    total_phone_size = sum(record.phone_size for record in records)
    total_file_size = sum(record.file_size for record in records)
    overall_total_size = sum(record.total_size for record in records)
    
    context = {
        'records': records,
        'total_name_size': total_name_size,
        'total_email_size': total_email_size,
        'total_phone_size': total_phone_size,
        'total_file_size': total_file_size,
        'overall_total_size': overall_total_size,
    }
    
    return render(request, 'show_data.html', context)
