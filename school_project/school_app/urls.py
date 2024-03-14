from django.urls import path
from . import views
from .views import SchoolLoginView, SchoolLogoutView, profile, ChangeUserInfoView, SchoolPasswordChangeView, \
    RegisterUserView, RegisterDoneView, user_activate, DeleteUserView, other_page, edu_page

urlpatterns = [
    path('', views.index, name='index'),
    #path('about/', views.about, name='about'),
    path('<str:page>/<str:page2>', edu_page, name='edu'),
    path('<str:page>/', other_page, name='other'),
    path('accounts/register/', RegisterUserView.as_view(),name='register'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(),name='register_done'),
    path('accounts/login/', SchoolLoginView.as_view(), name='login'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', SchoolLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', SchoolPasswordChangeView.as_view(), name='password_change'),
    ]
