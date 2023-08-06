from django.shortcuts import render, get_object_or_404
# importing a generic vie library
# View class provided by Django, gives us more control over handling HTTP
# methods like GET, POST, etc.
from django.views import generic, View
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


class PostDetail(View):
    # In Django's class-based views, the method that corresponds to a specific HTTP
    # request type (such as GET, POST, etc.) is determined by the name of the method

    # Method named get, is called when an HTTP GET request is made to the corresponding URL.

    # The self parameter refers to the instance of the PostDetail class, and the request
    # parameter represents the incoming HTTP request.

    # <slug:slug> in urls.py file is a path converter in Django's URL patterns. It's used to
    # capture a string of text from the URL and pass it as a parameter to the associated view
    # function.
    # The second slug in these angle brackets is a keyword name that matches the slug parameter
    # in the get method of the PostDetail class
    def get(self, request, slug, *args, **kwargs):
        # queryset is a variable that holds the initial queryset for retrieving posts from
        # the database. In this line, you're creating a queryset that filters the Post model
        # to include only those posts with a status value of 1
        queryset = Post.objects.filter(status=1)
        # Here we use this queryset to fetch a specific post based on the slug parameter:
        # This queryset is used to retrieve the specific post using the get_object_or_404
        # function, which returns a post with the provided slug or raises a 404 error if
        # the post is not found

        # Here, the post variable holds the instance of the Post model that matches the provided
        # slug. Once you have this post instance, you can access its attributes (fields) in the
        # template using the dot notation
        post = get_object_or_404(queryset, slug=slug)
        print(dir(post))
        # After obtaining the post, the comments associated with the post are filtered to
        # include only approved comments (those with approved=True) and ordered by their
        # creation date
        comments = post.comments.filter(approved=True).order_by('created_on')
        # The code checks whether the currently logged-in user (if any) has liked the post.
        # If the user's ID exists in the post's likes queryset, it means they have liked the
        # post
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # The template is rendered with the post object, the filtered comments queryset, and a
        # boolean liked variable that indicates whether the logged-in user has liked the post
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
