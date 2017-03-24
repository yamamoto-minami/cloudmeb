from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from cloudmeb.users.models import User

class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kargs):
        super(UserCreationForm, self).__init__(*args, **kargs)
        # del self.fields['username']

    class Meta:
        fields = '__all__'
        model = User

class UserChangeForm(BaseUserChangeForm):
    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)
        # del self.fields['username']

    class Meta:
        fields = '__all__'
        model = User