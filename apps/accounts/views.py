from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from apps.accounts.forms import UserRegisterForm, UserLoginForm


class ChooseWhoView(generic.TemplateView):
    template_name = 'choose_who.html'


# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     form_class = UserLoginForm
#     fields = '__all__'
#     redirect_authenticated_user = True
#
#     def get_success_url(self):
#         return reverse_lazy('user-list')
#
#
# class CustomLogoutView(LogoutView):
#     next_page = reverse_lazy('choose-who')


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
        return context
