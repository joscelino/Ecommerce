from django.contrib.auth.models import User
from django import forms
from .models import CostumerAddress


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CostumerAddress
        fields = '__all__'
        exclude = ('user', 'active')


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
    )

    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Password confirmation',
    )

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'password2', 'email')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        user_data = cleaned.get('username')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')
        email_data = cleaned.get('email')
        user_db = User.objects.filter(username=user_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'User already exists!'
        email_msg_user_exists = 'E-mail already exists!'
        password_msg_user_match = 'Passwords do not match!'
        password_msg_user_short = 'Password too short!'
        error_msg_required_field = 'Required field'

        if self.user:
            if user_db:
                if user_data != user_db.username:
                    validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                if email_data != email_db.email:
                    validation_error_msgs['email'] = email_msg_user_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = password_msg_user_match

            if len(password_data) < 6:
                validation_error_msgs['password'] = password_msg_user_short

        else:

            if user_db:
                validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                validation_error_msgs['email'] = email_msg_user_exists

            if not password_data:
                validation_error_msgs['password'] = error_msg_required_field

            if not password2_data:
                validation_error_msgs['password2'] = error_msg_required_field

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = password_msg_user_match

            if len(password_data) < 6:
                validation_error_msgs['password'] = password_msg_user_short

        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))




