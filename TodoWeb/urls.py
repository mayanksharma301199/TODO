from django.urls import path
from . import views
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('', views.Home, name = 'Home'),

    path('LogIn', views.LogIn, name = 'UserLogIn'),

    path('UserHome/NewTask', views.NewTask, name = 'NewTask'),

    path('SignUp', views.NewAccount, name = 'NewAccount'),

    path('UserHome', views.UserHome, name = 'UserHome'),

    # path(r'api-token-refresh/', refresh_jwt_token),

    # path('decodetoken', views.decode, name = "tokendecode")

    # path('LogIn', views.LogIn, name = 'LogIn'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('LogIn/<token>', views.LogIn, name = 'LogIn'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')


    
]