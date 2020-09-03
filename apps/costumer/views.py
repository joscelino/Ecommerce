from django.views import View
from django.shortcuts import render

from .models import Costumer
from .forms import UserForm, ProfileForm


class ProfileBase(View):
    template_name = 'costumer/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:

            context = {
                'userform': UserForm(
                    data=self.request.POST or None,
                    user= self.request.user,
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

        self.rendering = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.rendering


class CostumerCreation(ProfileBase):
    def post(self, *args, **kwargs):
        return self.rendering


class CostumerUpdate(View):
    pass


class CostumerLogin(View):
    pass


class CostumerLogout(View):
    pass
