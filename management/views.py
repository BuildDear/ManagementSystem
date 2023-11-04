from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from apps.accounts.forms import UserLoginForm


class StartView(generic.TemplateView):
    template_name = 'start.html'


class ChooseWhoView(generic.TemplateView):
    template_name = 'choose_who.html'


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    fields = ('email', 'password',)
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['button_label'] = 'Login'
        return context

    def get_form_kwargs(self):
        kwargs = super(CustomLoginView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('choose-who')
