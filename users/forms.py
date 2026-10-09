from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Faculty


class StudentRegisterForm(UserCreationForm):
    faculty = forms.ModelChoiceField(
        queryset=Faculty.objects.all(),
        required=True,
        label="Факультет",
        empty_label="-- Выберите ваш факультет --",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "full_name", "faculty")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email or not email.endswith("@iuca.kg"):
            raise forms.ValidationError("Регистрация разрешена только с корпоративной почтой @iuca.kg")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с такой почтой уже зарегистрирован.")
        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("full_name", "faculty", "bio", "avatar_url")
        labels = {
            "full_name": "ФИО",
            "faculty": "Факультет",
            "bio": "О себе",
            "avatar_url": "Ссылка на аватарку",
        }