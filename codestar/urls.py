"""codestar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # That will register our Summernote urls here  with our urls.py file. Now all
    # we need to do is tell our admin panel which field  we want to use Summernote for.

    # In this Django urlpatterns configuration, the path "summernote/" is mapped to
    # include the URLs provided by the "django_summernote.urls" module.

    # The "include" function allows you to include other URL configurations from different
    # apps into the main urlpatterns. Assuming you have installed the Django Summernote
    # package, when a user visits "/summernote/" in the browser, Django will handle the
    # request and navigate to the Django Summernote views and templates.

    path('summernote/', include("django_summernote.urls"))
]
