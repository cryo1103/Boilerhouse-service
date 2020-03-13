from django.http import HttpResponse

def index(request):
    return HttpResponse("данные на юзверя")

def application(request):
    return HttpResponse("тут вводится заявка юзверя")

