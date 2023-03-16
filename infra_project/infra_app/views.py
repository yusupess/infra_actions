from django.http import HttpResponse


def index(request):
    return HttpResponse('Все работает как надо!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
