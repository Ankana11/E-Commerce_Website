from django.urls import path
from authcart import views


urlpatterns = [
    path('signup',views.Signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    # path('profile',views.profile,name="profile"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]
