from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path('accounts/',include('allauth.urls')),
    path('auth/', obtain_jwt_token),

]
