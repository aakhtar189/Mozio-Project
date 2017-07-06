from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.db.models import Q, Count

from supplier.models import Supplier
from supplier.forms import AddSupplierForm, EditSupplierForm


def homepage(request):
    if not request.user.is_authenticated():
        return redirect(reverse('login_user'))

    suppliers =  Supplier.objects.all().order_by('-created')

    query = request.GET.get('q', '')

    if query:
        suppliers = suppliers.filter(name__icontains=query).order_by('-created')

    context = {
        "query": query,
        "suppliers": suppliers
    }

    return render(request, "homepage.html", context)


@login_required
def add_supplier(request):
    if not request.user.is_superuser:
        return redirect("/")

    form = AddSupplierForm(use_required_attribute=False)

    if request.method == "POST":
        form = AddSupplierForm(request.POST or None, use_required_attribute=False)

        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
            )

            supplier_obj = Supplier.objects.create(
                user=user,
                name=user.username,
                phone_no=form.cleaned_data["phone_no"],
                language=form.cleaned_data["language"],
                currency=form.cleaned_data["currency"]
            )
            return redirect(reverse('homepage'))

        else:
            for key, value in form.errors.items():
                tmp = {'key': key, 'error': value.as_text()}

    return render(request, "supplier/create_supplier.html", {"form": form})


@login_required
def edit_supplier(request, supplier_id):
    if not request.user.is_superuser:
        return redirect("/")

    supplier_obj = Supplier.objects.get(id=supplier_id)

    if request.method == "POST":
        form = EditSupplierForm(request.POST, instance=supplier_obj, use_required_attribute=False)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(reverse('homepage'))

        return render(request, "supplier/create_supplier.html", {
            "form": form,
            "supplier_obj": supplier_obj,
        })

    else:
        form = EditSupplierForm(instance=supplier_obj, use_required_attribute=False)

        return render(request, "supplier/create_supplier.html", {
            "current": "edit_property",
            "form": form,
            "supplier_obj": supplier_obj,
        })


@login_required
def delete_supplier(request, supplier_id):
    if not request.user.is_superuser:
        return redirect("/")

    supplier_obj = Supplier.objects.get(id=supplier_id)
    supplier_obj.user.delete()

    return redirect("/")