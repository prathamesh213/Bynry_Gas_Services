from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def home(request):
    return render(request, 'home.html')



def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('service_requests:request_status', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

def request_status(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk)
    return render(request, 'service_requests/request_status.html', {'service_request': service_request})
