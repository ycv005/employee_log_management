from django.views import generic
from .admin import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import forms, logout, login
from django.http import HttpResponseRedirect


class SignUpView(generic.CreateView):
    """
    View to handle user's signup
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login_page')
    template_name = 'registration/signup.html'


class LoginView(generic.FormView):
    """
    View to handle user's login
    """
    form_class = forms.AuthenticationForm
    success_url = reverse_lazy('home-page')
    template_name = 'registration/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


def logout_view(request):
    """
    View to handle logout
    """
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home-page'))
