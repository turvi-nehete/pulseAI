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