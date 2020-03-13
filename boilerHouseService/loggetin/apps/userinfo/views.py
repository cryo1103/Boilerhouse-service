from django.http import HttpResponse


def index(request):
    return HttpResponse("личный кабинет юзверя")


def application(request):
    return HttpResponse("тут вводится заявка юзверя")


