from django.http import HttpResponse


def connect_calendar(request):
    return HttpResponse("Connect Calendar")


def create_meeting(request):
    return HttpResponse("Create Meeting")