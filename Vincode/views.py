from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel, Item,hotai
from django.core import serializers
from .form import SearchForm
from django.views import View
from django.db.models import Q
import re

def extract_numeric_from_string(s):
    # 使用正則表達式匹配字符串中的數字部分
    match = re.search(r'\d+', s)
    
    if match:
        # 如果找到匹配，返回數字部分的字符串
        return match.group()
    else:
        # 如果未找到匹配，返回None
        return None
    

def home(request):
    form = SearchForm(request.GET)
    datas = None
    error_message = None
    user_input = None

    if form.is_valid():
        search_term = form.cleaned_data.get('search_term')
        user_input = search_term  

        if search_term and len(search_term) == 17:
            vis_code = search_term[10]   # 根據條件取得第11或第13位的數字

            if vis_code.isdigit():
                # 第 10 位是數字
                wmi = search_term[:3]
                vds = search_term[3:8]
                validation = search_term[8:10]
                vis_code1 = search_term[10:]

                try:
                    # 使用 __startswith 進行模糊搜尋
<<<<<<< HEAD
                    items = CombineLexus.objects.filter(
                        Q(WMI=wmi) & Q(VDS=vds) & Q(VALADATION=validation) &(
                            Q(VIS_min__lte=int(vis_code1)) & Q(VIS_max__gt=int(vis_code1))
=======
                    items = hotai.objects.filter(
                        Q(WMI=wmi) & Q(VDS=vds) & (
                            Q(VIS_min__lte=int(vis_code1)) & Q(VIS_max__gte=int(vis_code1))
>>>>>>> 16ecf7644890736520908a9d6f32d848b37ba87d
                        )
                    )
                    
                    # 從搜尋結果中找到符合條件的項目
                    if items.exists():
                        datas = [items.first()]
                    else:
                        error_message = "VIN does not meet the specified conditions."

<<<<<<< HEAD
                except CombineLexus.DoesNotExist:
=======
                except hotai.DoesNotExist:
>>>>>>> 16ecf7644890736520908a9d6f32d848b37ba87d
                    error_message = "No data found for the given search term."
            elif vis_code.isalpha():
                # 第 10 位是字母
                wmi = search_term[:3]
                vds = search_term[3:8]
<<<<<<< HEAD
                validation = search_term[8:10]
                validation2 = search_term[10]
=======
                validation = search_term[10]
>>>>>>> 16ecf7644890736520908a9d6f32d848b37ba87d
                vis_code1 = search_term[11:]

                try:
                    # 使用 __startswith 進行模糊搜尋，同時添加虛擬欄位 'numeric_code'
<<<<<<< HEAD
                    items = CombineLexus.objects.filter(
                        Q(WMI=wmi) & Q(VDS=vds) & Q(VALADATION=validation) & Q(VIS_min__startswith=str(validation2)) &(
                            Q(VIS_min_false__lte=int(vis_code1)) & Q(VIS_max_false__gt=int(vis_code1))
=======
                    items = hotai.objects.filter(
                        Q(WMI=wmi) & Q(VDS=vds) & Q(TOYOTA進口_VALADATION = validation) & (
                            Q(VIS_min_false__lte=int(vis_code1)) & Q(VIS_max_false__gte=int(vis_code1))
>>>>>>> 16ecf7644890736520908a9d6f32d848b37ba87d
                        )
                    )
                        
                    # 從搜尋結果中找到符合條件的項目
                    if items.exists():
                        datas = [items.first()]
                    else:
                        error_message = "VIN does not meet the specified conditions."

<<<<<<< HEAD
                except CombineLexus.DoesNotExist:
=======
                except hotai.DoesNotExist:
>>>>>>> 16ecf7644890736520908a9d6f32d848b37ba87d
                    error_message = "No data found for the given search term."
            else:
                print("Invalid VIN format. Unexpected condition.")
                error_message = "Invalid VIN format. Unexpected condition."

    return render(request, 'index.html', {'form': form, 'datas': datas, 'user_input': user_input, 'error_message': error_message})
