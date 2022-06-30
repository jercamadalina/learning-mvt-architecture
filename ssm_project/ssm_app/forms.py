from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    #     fields = ('username', 'password1', 'password2', 'date_of_birth')
    #
    # biography = forms.CharField()
    #
    # def save(self, commit=True):
    #     result = super().save(commit=commit)  # metoda save creaza un user
    #     if commit:
    #         bio = self.cleaned_data['biography']
    #         profile = Profile.objects.create(user=result, biography=bio)
    #
    #     return result