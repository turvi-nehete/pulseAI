from django.http import HttpResponse


def chat(request):
    return HttpResponse("AI Chat")


def generate_email(request):
    return HttpResponse("Generate Email")