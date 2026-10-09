from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Faculty


class StudentRegisterForm(UserCreationForm):
    faculty = forms.ModelChoiceField(
        queryset=Faculty.objects.all(),
        required=False,
        label="Факультет",
        empty_label="Выберите факультет"
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