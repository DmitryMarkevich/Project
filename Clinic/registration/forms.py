from django import forms

from Clinic_info.models import Service, Client


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].empty_label = "Категория не выбрана"

    class Meta:
        model = Client
        fields = '__all__'

    # name = forms.CharField(max_length=60,
    #                        widget=forms.TextInput(attrs={"class": "form-control",
    #                                                      "placeholder": "Ваше имя"}))
    # telephone = forms.CharField(max_length=20,
    #                             widget=forms.TextInput(attrs={"class": "form-control",
    #                                                           "placeholder": "+375 (___) ___-__-__"}))
    # email = forms.EmailField(max_length=100,
    #                          widget=forms.TextInput(attrs={"class": "form-control",
    #                                                        "placeholder": "Email"}))
    # service = forms.ModelChoiceField(queryset=Service.object.all(),
    #                                  widget=forms.TextInput(attrs={"class": "form-control",
    #                                                                "placeholder": "Выберите сервис"}))
