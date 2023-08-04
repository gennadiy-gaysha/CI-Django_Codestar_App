from . import views
from django.urls import path

# To make sure Django's URL dispatcher knows how to route requests correctly,
# you need to establish a clear connection between the project-level urls.py and
# the app-level urls.py files. This connection is achieved by using the include()
# function in the project-level urls.py.
urlpatterns = [
    # because we're using class-based views we need to add the as_view method
    path('', views.PostList.as_view(), name="home"),
]
