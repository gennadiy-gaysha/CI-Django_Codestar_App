from . import views
# This line imports the path function from Django's URL handling module.
from django.urls import path

# To make sure Django's URL dispatcher knows how to route requests correctly,
# you need to establish a clear connection between the project-level urls.py and
# the app-level urls.py files. This connection is achieved by using the include()
# function in the project-level urls.py.
urlpatterns = [
    # because we're using class-based views we need to add the as_view method
    path('', views.PostList.as_view(), name="home"),
    # In the URL pattern <slug:slug>, the first instance of "slug" is a path converter,
    # and the second instance of "slug" is the name of the parameter that will be passed
    # to the view function.
    # <slug:slug> is a path converter in Django's URL patterns

    # The first slug in angle  brackets is called a path converter. The second slog is
    # a keyword name. Now this could be anything we wanted, but  to keep it consistent we're
    # calling it slug. The path converter converts this text into a slug  field, it tells
    # Django to match any slug string, which consists of ASCII characters or numbers  plus
    # the hyphen and underscore characters.

    # <slug:slug> in urls.py file is a path converter in Django's URL patterns. It's used to
    # capture a string of text from the URL and pass it as a parameter to the associated view
    # function.
    # The second slug in these angle brackets is a keyword name that matches the slug parameter
    # in the get method of the PostDetail class
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')

]
