import logging

from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views import generic

from apps.accounts.forms import UserRegisterForm, UserLoginForm

logger = logging.getLogger(__name__)


class ChooseWhoView(generic.TemplateView):
    template_name = 'choose_who.html'


class ManagerRegisterView(generic.CreateView):
    template_name = 'registration.html'
    form_class = UserRegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_manager = True
        self.object.set_password(form.cleaned_data['password'])
        group = form.cleaned_data.get('group', None)
        if group:
            self.object.group = group

        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Manager Registration'
        context['button_label'] = 'Create'
        context['is_manager'] = True
        return context


class UserRegisterView(generic.CreateView):
    template_name = 'registration.html'
    form_class = UserRegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_manager = False
        self.object.set_password(form.cleaned_data['password'])
        group = form.cleaned_data.get('group', None)
        if group:
            self.object.group = group

        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User Registration'
        context['button_label'] = 'Create'
        context['is_manager'] = False
        return context


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    form_class = UserLoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Authorization'
        context['button_label'] = 'Login'

        # Додавання запису до журналу
        logger.info("Отримано контекст для Manager Login")

        return context

    def form_valid(self, form):
        # Логування перед викликом базової реалізації
        logger.info(f"Успішна авторизація для користувача {form.get_user()}")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Логування невдалої спроби авторизації
        logger.warning("Невдала спроба авторизації")
        return super().form_invalid(form)

    def get_success_url(self):
        logger.info(f"Перенаправлення на {'user-list'}")
        return reverse_lazy('user-list')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('choose-who')
