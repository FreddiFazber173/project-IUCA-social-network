from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegisterForm, ProfileUpdateForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно! Добро пожаловать.")
            return redirect("profile")
        else:
            messages.error(request, "Ошибка при регистрации. Проверьте введенные данные.")
    else:
        form = StudentRegisterForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен!")
            return redirect("profile")
        else:
            messages.error(request, "Не удалось обновить профиль. Проверьте данные.")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "users/profile.html", {"profile_form": form})