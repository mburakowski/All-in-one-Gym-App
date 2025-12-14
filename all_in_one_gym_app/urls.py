from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Bezpośrednie renderowanie base.html na stronie głównej
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
]