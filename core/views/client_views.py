from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404

from core.models import Client
from core.forms import ClientForm

#add (inbuild django model form which validates better than manually doing that )plus show client
@login_required
def clients(request):

    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():

            client = form.save(commit=False)
            client.uid = request.user
            client.save()
            return redirect("clients")

    else:

        form = ClientForm()

    client_list = Client.objects.filter(
        uid=request.user
    ).order_by("-created_at")

    context = {
        "clients": client_list,
        "form": form,
    }

    return render(
        request,
        "clients.html",
        context
    )


from django.shortcuts import render, redirect, get_object_or_404

@login_required
def edit_client(request, cid):

    client = get_object_or_404(
        Client,
        cid=cid,
        uid=request.user
    )

    if request.method == "POST":

        form = ClientForm(
            request.POST,
            instance=client
        )

        if form.is_valid():
            form.save()
            return redirect("clients")

    return redirect("clients")


@login_required
def delete_client(request, cid):

    client = get_object_or_404(
        Client,
        cid=cid,
        uid=request.user
    )

    client.delete()

    return redirect("clients")


import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from core.models import Client


@require_POST
def get_recipients(request):

    data = json.loads(request.body)

    customer_type = data.get("customer_type", "").strip()
    company_type = data.get("company_type", "").strip()
    country = data.get("country", "").strip()
    state = data.get("state", "").strip()
    city = data.get("city", "").strip()

    clients = Client.objects.filter(
        uid=request.user,
        is_active=True
    )

    if customer_type:
        clients = clients.filter(customer_type__iexact=customer_type)

    if company_type:
        clients = clients.filter(comp_type__iexact=company_type)

    if country:
        clients = clients.filter(country__iexact=country)

    if state:
        clients = clients.filter(state__iexact=state)

    if city:
        clients = clients.filter(city__iexact=city)

    recipient_list = []

    for client in clients:
        recipient_list.append({
            "id": client.cid,
            "name": client.contactname,
            "company": client.comp_name,
            "email": client.c_mail,
        })

    return JsonResponse({
        "count": len(recipient_list),
        "recipients": recipient_list,
    })