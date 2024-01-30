from django.shortcuts import render


def main_page(request):
    """Главная страница"""
    return render(request, 'index.html')
