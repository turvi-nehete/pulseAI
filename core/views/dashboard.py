from django.http import HttpResponse



def dashboard_data(request):
    return HttpResponse("Dashboard")
