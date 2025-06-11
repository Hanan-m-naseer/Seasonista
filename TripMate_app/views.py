from django.shortcuts import render,get_object_or_404, redirect
from rest_framework import viewsets
from .models import Destination, DestinationImage
from .serializers import DestinationSerializer, DestinationImageSerializer
from .forms import DestinationForm, DestinationImageForm


# Create your views here.

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationImageViewSet(viewsets.ModelViewSet):
    queryset = DestinationImage.objects.all()
    serializer_class = DestinationImageSerializer

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'TripMate_app/destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'TripMate_app/destination_detail.html', {'destination': destination})

def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm()
    return render(request, 'TripMate_app/destination_form.html', {'form': form})

def upload_images(request, pk):
    destination = get_object_or_404(Destination, pk=pk)

    if request.method == 'POST':
        form = DestinationImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.destination = destination
            image.save()
            return redirect('destination_detail', pk=pk)
    else:
        form = DestinationImageForm()

    return render(request, 'TripMate_app/image_upload.html', {
        'form': form,
        'destination': destination
    })

def home(request):
    return render(request, 'TripMate_app/home.html')
