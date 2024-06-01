from django.urls import path

from knox import views as knox_views

from .views import CreateUserView, LoginView, ManageUserView, me, account

app_name = 'core'

urlpatterns = [
    path ('me/', me, name="me",),
    path ('account/', account, name="account",),
    path('create/', CreateUserView.as_view(), name="create"),
    path('profile/', ManageUserView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]