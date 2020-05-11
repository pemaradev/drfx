from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
# from django.views.generic import TemplateView, RedirectView

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Documentación de comercio')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
    # url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    path('api/docs/', schema_view),
]
