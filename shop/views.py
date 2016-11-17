from django.shortcuts import render
from shop.models import CategoryModel, ItemModel
from django.views import View



def index(request):
    return render(request, 'index.html', {'var_name': "Полина"})


def shopping(request):
    data = CategoryModel.objects.all()
    return render(request, 'product.html', context={'menu': data})


class NewView(View):
    def get(self, request):
        data_search_n = ItemModel.objects.filter(category_id=1).all()
        if len(data_search_n) == 0:
            return render(request, 'search-empty.html')
        else:
            return render(request, 'search.html', context={'search': data_search_n})


class BasicView(View):
    def get(self, request):
        data_search_b = ItemModel.objects.filter(category_id=2).all()
        if len(data_search_b) == 0:
            return render(request, 'search-empty.html')
        else:
            return render(request, 'search.html', context={'search': data_search_b})


class SaleView(View):
    def get(self, request):
        data_search_n = ItemModel.objects.filter(category_id=3).all()
        if len(data_search_n) == 0:
            return render(request, 'search-empty.html')
        else:
            return render(request, 'search.html', context={'search': data_search_n})
