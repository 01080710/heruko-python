from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel, Item,CombineLexus
from django.core import serializers
from .form import SearchForm
from django.views import View


# Create your views here.
def home(request):
    form = SearchForm(request.GET)
    data = None

    if form.is_valid():
        search_term = form.cleaned_data.get('search_term')

        if search_term:
            try:
                item = CombineLexus.objects.filter(VIN=search_term).first()
                data = CombineLexus.objects.filter(VIN=search_term)
            except CombineLexus.DoesNotExist:
                error_message = "No data found for the given search term."
                return render(request, 'index.html', {'form': form, 'error_message': error_message})
    
    if data is None:
        error_message = "Input is incorrect."

    return render(request, 'index.html', {'form': form, 'datas': data})

