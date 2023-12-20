#<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel, Item,CombineLexus
from django.core import serializers
from .form import SearchForm
from django.views import View
from django.db.models import Q

# Create your views here.
#def home(request):
    #form = SearchForm(request.GET)
    #data = None

    #if form.is_valid():
      #  search_term = form.cleaned_data.get('search_term')

      #  if search_term:
         #   try:
             #   item = CombineLexus.objects.get(VIN=search_term)
             #   data = CombineLexus.objects.filter(VIN=search_term)
           # except CombineLexus.DoesNotExist:
                #error_message = "No data found for the given search term."
               # return render(request, 'index.html', {'form': form, 'error_message': error_message})
    
   # if data is None:
       # error_message = "Input is incorrect."

   # return render(request, 'index.html', {'form': form, 'datas': data})


def home(request):
    form = SearchForm(request.GET)
    datas = None
    error_message = None
    user_input = None

    if form.is_valid():
        search_term = form.cleaned_data.get('search_term')
        user_input = search_term  # 將用戶輸入的值保存到 user_input 變數中

        if search_term and len(search_term) == 17:
            wmi = search_term[:3]
            vds = search_term[3:8]
            valadation = search_term[8:10]
            vis_code = search_term[10::]  # 取得第11位的數字

            try:
                # 使用 __startswith 進行模糊搜尋
                items = CombineLexus.objects.filter(
                    Q(WMI=wmi) & Q(VDS=vds) &  Q(VALADATION=valadation) & Q(VIS_min__lte=int(vis_code)) & Q(VIS_max__gte=int(vis_code))
                )

                # 從搜尋結果中找到符合條件的項目
                #valid_items = [item for item in items if item.WMI == wmi and item.VDS == vds and item.VIS_min <= int(vis_code) <= item.VIS_max]

                if items.exists():
                    datas = [items.first()]
                else:
                    error_message = "VIN does not meet the specified conditions."

            except CombineLexus.DoesNotExist:
                error_message = "No data found for the given search term."

    if datas is None and error_message is None:
        error_message = "Input is incorrect."

    return render(request, 'index.html', {'form': form, 'datas': datas,'user_input': user_input})