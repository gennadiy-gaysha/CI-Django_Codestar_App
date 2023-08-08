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

    path('summernote/', include("django_summernote.urls")),

    # In the project-level urls.py, use the include() function to include the app's URL
    # patterns. This effectively delegates the URL routing for that app to its own urls.py file.

    # By including the app-level urls.py files within the project-level urls.py, you establish
    # the necessary connection. Django's URL dispatcher will navigate requests through this
    # connection to the appropriate views based on the URL patterns defined in the app-level
    # urls.py files.

    #  the project-level urls.py uses the include() function to route the request to the app-level
    #  urls.py. The app-level urls.py then further routes the request to the appropriate view,
    #  such as MyAppView. This connection ensures that Django's URL dispatcher knows how to route
    #  requests correctly throughout the project.
    path('', include('blog.urls'), name='blog_urls'),
    #  This is used to include the URL patterns provided by the Django Allauth app into your
    # project's main URL configuration

    # When you include the Allauth URL patterns in this manner, it means that when users visit
    # URLs like /accounts/login/, /accounts/signup/, or /accounts/password/reset/, the Allauth
    # views associated with these URLs will be invoked.
    path('accounts/', include('allauth.urls'))
]
