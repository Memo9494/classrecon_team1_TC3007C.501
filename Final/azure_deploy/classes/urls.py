from django.urls import path
from .views import SignUpView, CustomLoginView, custom_login

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    #login with cusom_login
    path('login/', custom_login, name='login'),

]
