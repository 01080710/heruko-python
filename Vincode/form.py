from django import forms



class SearchForm(forms.Form):
    search_term = forms.CharField(label='Search', max_length=17, required=False)
    # 其他查詢條件...

    def clean_search_term(self):
        search_term = self.cleaned_data.get('search_term')

        if search_term and len(search_term) != 17:
            raise forms.ValidationError("Search term must be 17 characters long.")

        return search_term
