from django.shortcuts import render
# importing a generic vie library
from django.views import generic
from .models import Post

# Create your views here.

# class PostList(generic.ListView): This class inherits from generic.ListView, which
# is a generic class-based view provided by Django for displaying a list of objects.


class PostList(generic.ListView):
    # model = Post: This line specifies the model that the view will be working with.
    # In this case, it's the Post model. By setting the model attribute, you're telling
    # Django that the view is going to work with the Post model's data.

    # !!!the model attribute is set in the PostList class
    model = Post
    # A queryset in Django is a representation of a database query. It's essentially a list of
    # database records returned from the database based on the conditions and filters defined in
    # the queryset.
    # This line defines the queryset that the view will use to fetch the data from the database.
    # The Post.objects part refers to the manager for the Post model, which provides methods for
    # querying the database.
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # template_name attribute is an attribute of the ListView class
    template_name = 'index.html'
    # paginate_by is also an attribute of the ListView class in Django.
    paginate_by = 6
