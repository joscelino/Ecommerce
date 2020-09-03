from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

import copy

from .models import CostumerAddress
from .forms import UserForm, ProfileForm


class ProfileBase(View):

    rendering: HttpResponse
    template_name = 'costumer/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.cart = copy.deepcopy(self.request.session.get('cart', {}))

        self.profile = None

        if self.request.user.is_authenticated:
            self.profile = CostumerAddress.objects.filter(user=self.request.user).first()

            if self.request.user.is_authenticated:
                self.context = {
                    'userform': UserForm(
                        data=self.request.POST or None,
                        user=self.request.user,
                        instance=self.request.user,
                    ),
                    'profileform': ProfileForm(
                        data=self.request.POST or None,
                        instance=self.profile
                    ),
                }

        else:
            self.context = {
                'userform': UserForm(
                    data=self.request.POST or None,
                ),
                'profileform': ProfileForm(
                    data=self.request.POST or None
                ),
            }

        self.userform = self.context['userform']
        self.profileform = self.context['profileform']

        if self.request.user.is_authenticated:
            self.template_name = 'costumer/update.html'

        self.rendering = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.rendering


class CostumerCreation(ProfileBase):
    def post(self, *args, **kwargs):

        if not self.userform.is_valid() or not self.profileform.is_valid():
            return self.rendering

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        if self.request.user.is_authenticated:
            user = get_object_or_404(User, username=self.request.user.username)
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name

            if password:
                user.set_password(password)

            user.save()

            if not self.profile:
                self.profileform.cleaned_data['user'] = user
                profile = CostumerAddress(**self.profileform.cleaned_data)
                profile.save()
            else:
                profile = self.profileform.save(commit=False)
                profile.user = user
                profile.save()

        else:
            user = self.userform.save(commit=False)
            user.set_password(password)
            user.save()

            profile = self.profileform.save(commit=False)
            profile.user = user
            profile.save()

        if password:
            authentication = authenticate(
                self.request,
                username=user,
                password=password,
            )

        if authentication:
            login(self.request, user=user)

        self.request.session['cart'] = self.cart
        self.request.session.save()

        messages.success(
            self.request,
            'Your account was created/updated with success!'
        )
        return redirect('costumer:create')


class CostumerLogin(View):
    def post(self, *args, **kwargs):

        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(
                self.request,
                'Invalid login!'
            )
            return redirect('costumer:create')

        user = authenticate(
            self.request,
            username=username,
            password=password,
        )

        if not user:
            messages.error(
                self.request,
                'Invalid user!'
            )

        login(self.request, user=user)
        messages.success(
            self.request,
            'Login successfully!'
        )

        return redirect('product:cart')


class CostumerLogout(View):
    def get(self, *args, **kwargs):

        logout(self.request)

        cart = copy.deepcopy(self.request.session.get('cart', {}))
        if cart:
            self.request.session['cart'] = cart
            self.request.session.save()

        messages.success(
            self.request,
            'Logout with success!'
        )

        return redirect('product:list')
