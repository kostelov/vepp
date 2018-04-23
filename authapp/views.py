from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from vepp import settings
from authapp.forms import UserFormLogin


def login(request):
    title = 'Вхід'
    form = UserFormLogin()
    if request.method == 'POST':
        form = UserFormLogin(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user and user.is_active and user.is_superuser:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('admin'))
            elif user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
            else:
                return HttpResponseRedirect(reverse('main'))

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


# class LoginFormView(FormView):
#     form_class = UserFormLogin
#     # initial = {'username': 'username', 'password': 'password'}
#     # fields = ('username', 'password',)
#     template_name = 'authapp/login.html'
#     success_url = reverse_lazy('main')
#
#     # def get(self, request, *args, **kwargs):
#     #     form = self.form_class()
#     #     return render(request, self.template_name, {'form': form})
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         form = context['form']
#         for field_name, field in form.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
#         context['form'] = form
#         context['title'] = 'Вхід'
#         return context
#
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(request, username=username, password=password)
#             print(user)
#             print(username)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('main'))
#                 # return render(request, self.success_url)
#             else:
#                 return HttpResponseRedirect(reverse('main'))
#             # return render(request, self.success_url)
#
#         return render(request, self.template_name, {'form': form})


def logout(request):
    auth.logout(request)
    # return HttpResponseRedirect(reverse('auth:login'))
    return HttpResponseRedirect(settings.LOGIN_URL)
