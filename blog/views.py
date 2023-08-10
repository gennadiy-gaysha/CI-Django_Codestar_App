from django.shortcuts import render, get_object_or_404, reverse
# importing a generic vie library
# View class provided by Django, gives us more control over handling HTTP
# methods like GET, POST, etc.
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm

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
                # when a user visits the page to view a post, the "commented" context variable is set to False. This is because no comment has been submitted yet; the user is just viewing the post and its comments. This sets up the initial state of the variable when the page loads.
                "commented": False,
                "liked": liked,
                # So with the form imported, we now  need to render it as part of our view.
                # To do this, we can simply add it to our context:
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        # retrieves the post based on the provided slug from the URL.
        post = get_object_or_404(queryset, slug=slug)
        # filters and orders the approved comments for the post.
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        # checks whether the logged-in user has liked the post.
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # We need to get the  data from our form and assign it to a variable.
        # So I'm going to create a  new variable here called comment_form.
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # checks if the submitted form data is valid. If it is, it sets the email and name
            # fields of the comment instance to the user's email and username.
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            # It saves the comment instance with the post association.
            comment = comment_form.save(commit=False)
            comment.post=post
            comment.save()
        else:
            # If the form data is not valid, it creates an empty comment_form to be rendered.
            comment_form = CommentForm()

        # renders the post_detail.html template with the updated context, including the comment form.
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                # after a user submits a comment, the "commented" context variable is set to True. This change in value indicates that a comment has been successfully submitted, and it allows you to show a message or modify the behavior of the template to reflect this state change.
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,

            },
        )


# This view specifically handles HTTP POST requests. It means that when a user interacts with the page to like or unlike a post, a POST request is sent to the server, and this view is responsible for processing that request.

#  this view is responsible for toggling the like/unlike status of a post based on user interaction and then redirecting the user back to the post's detail page.
class PostLike(View):
    # The slug parameter in the post method indicates that the URL for this view includes a slug value,
    # which likely identifies the specific post being liked or unliked.
    def post(self, request, slug):
        # The view starts by checking whether the user has already liked the post. It does this by using the likes attribute of the post object and checking if the user's ID exists in the set of likes. This is done using the filter and exists methods.
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            # If the user has already liked the post (post.likes.filter(id=request.user.id).exists() returns True), it means they want to unlike it. In that case, the user is removed from the list of likes using the remove method.
            post.likes.remove(request.user)
        else:
            # If the user has not liked the post (post.likes.filter(id=request.user.id).exists() returns False), it means they want to like it. In this case, the user is added to the list of likes using the add method.
            post.likes.add(request.user)
        # the view redirects the user to the post_detail page for the same post. This is achieved by using the HttpResponseRedirect class and the reverse function to generate the URL for the post_detail view, passing the slug as an argument.
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


