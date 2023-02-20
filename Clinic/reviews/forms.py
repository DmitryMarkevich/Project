from django import forms


class ReviewsForm(forms.Form):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={"class": "form-control",
                                                         "placeholder": "Ваше имя"}))
    review = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
                                                          "placeholder": "Оставьте отзыв"}))
