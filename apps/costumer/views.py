from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404

import copy

from .models import Costumer
from .forms import UserForm, ProfileForm


class ProfileBase(View):
    rendering: HttpResponse
    template_name = 'costumer/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.profile = None

        if self.request.user.is_authenticated:
            self.profile = Costumer.objects.filter(user=self.request.user).first()

            if self.request.user.is_authenticated:
                context = {
                    'userform': UserForm(
                        data=self.request.POST or None,
                        user=self.request.user,
                        instance=self.request.user,
                    ),
                    'profileform': ProfileForm(
                        data=self.request.POST or None
                    ),
                }


        else:

            context = {
                'userform': UserForm(
                    data=self.request.POST or None,
                ),
                'profileform': ProfileForm(
                    data=self.request.POST or None
                ),
            }

        self.userform = context['userform']
        self.profileform = context['profileform']

        self.rendering = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.rendering


class CostumerCreation(ProfileBase):
    def post(self, *args, **kwargs):

        if not self.userform.is_valid() or not self.profileform.is_valid():
            return self.rendering

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data('first_name')
        last_name = self.userform.cleaned_data('last_name')

        if self.request.user.is_authenticated:
            user = get_object_or_404(User, username=self.request.user.username)
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name

            if password:
                user.set_password(password)

            user.save()

        else:
            user = self.userform.save(commit=False)
            user.set_password(password)
            user.save()

            profile = self.profileform.save(commit=False)
            profile.user = user
            profile.save()

        return self.rendering


class CostumerUpdate(View):
    pass


class CostumerLogin(View):
    pass


class CostumerLogout(View):
    pass
