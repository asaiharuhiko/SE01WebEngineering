from .models import UserAccount
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class UserAccountLoginForm(AuthenticationForm):
    pass

class UserAccountCreateForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ["username"]
