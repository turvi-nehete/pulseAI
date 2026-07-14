from django.http import HttpResponse


def connect_gmail(request):
    return HttpResponse("Connect Gmail")


def gmail_callback(request):
    return HttpResponse("Gmail Callback")


def send_email(request):
    return HttpResponse("Send Email")