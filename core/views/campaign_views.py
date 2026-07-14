from django.http import HttpResponse


def create_campaign(request):
    return HttpResponse("Create Campaign")


def list_campaigns(request):
    return HttpResponse("List Campaigns")