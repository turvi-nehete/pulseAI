from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import Client


@login_required
def clients(request):

    client_list = Client.objects.filter(
        uid=request.user
    ).order_by("-created_at")

    print(client_list)

    context = {
        "clients": client_list
    }

    return render(
        request,
        "clients.html",
        context
    )