from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings

from account.forms import LoginForm
        

def login_user(request):

    if request.user.is_authenticated():
        return redirect(reverse('homepage'))

    form = LoginForm(request.POST or None, use_required_attribute=False)

    if request.method == "POST":

        if form.is_valid():
            user_obj = User.objects.get(email=form.cleaned_data['email'])
            user = authenticate(username=user_obj.username, password=form.cleaned_data['password'])

            if user:
                if user.is_active:
                    login(request, user)

                    return redirect(reverse('homepage'))

                return redirect(reverse('login_user'))
            else:

                error_message = "* Password you entered is incorrect."

                return render(request, "account/login_user.html",{
                    "form": form,
                    "error_message": error_message,
                })
        else:
            for key, value in form.errors.items():
                tmp = {'key': key, 'error': value.as_text()}

            return render(request, "account/login_user.html",{
                "form": form,
            })
    else:
        return render(request, "account/login_user.html", {
            "form": form,
        })


def logout_user(request):

    logout(request)
    return redirect(reverse('login_user'))


