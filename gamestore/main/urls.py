from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthenticationForm

# according to the tut im following , it used to login but now its LoginView/LougoutView

urlpatterns = [
    path(r'', views.index, name='index'),
    path('accounts/login/', LoginView.as_view(template_name='login.html',
                                              authentication_form=AuthenticationForm), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
]
# path(r'accounts/login/', LoginView, {
#     'template_name': 'login.html',
#     'authentication_form': AuthenticationForm}, name='login'),
