"""kanban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from rest_framework import routers
from terello import views
from django.contrib import admin
from django.views.generic import TemplateView


router = routers.DefaultRouter()
# router.register(r'^api', views.TaskViewSet)
# router.register(r'terello', TemplateView.as_view(template_name="index.html"))
router.register(r'tasks', views.TaskViewSet)
# router.register(r'^api/tasks/(?P<id>[0-9]+)', views.TaskViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^admin/', admin.site.urls),
#     url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
#     url(r'^$', TemplateView.as_view(template_name="index.html")),
#
# ]
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
