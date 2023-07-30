from django.db import models

# In Django, the User model is a pre-built model that represents a user account.
# It contains fields such as username, email, password, and more, which are commonly
# used to manage user authentication and access control in web applications.
from django.contrib.auth.models import User

# CloudinaryField is a special field provided by the "django-cloudinary-storage"
# library. By using CloudinaryField, you can easily handle image and media uploads,
# transformations, and optimizations without the need for additional server-side code.
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Publisshed"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        #   User: The User model is imported from django.contrib.auth.models, and it
        #   represents a registered user in the application. It is part of Django's
        #   built-in authentication system.

        #   on_delete=models.CASCADE: This attribute specifies the behavior when the related
        #   User instance is deleted. In this case, it's set to CASCADE, which means that if
        #   a user is deleted, all the blog posts authored by that user will also be deleted.

        #   related_name="blog_posts": This attribute defines the reverse relationship from
        #   User to Post. It sets the name of the attribute that can be used to access the set
        #   of blog posts created by a specific user. In this case, the related name is
        #   "blog_posts," so you can access the posts of a user with user.blog_posts.all().
        User, on_delete=models.CASCADE, related_name="blog_posts")
   #  When you use auto_now=True, Django takes care of setting the updated_on field value
   #  automatically, so you don't need to assign a value to it explicitly in your code.
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default="placeholder")
   #  blank=True: This attribute is set to True, which means that the excerpt field is not
   #  required and can be left empty (blank) when creating or updating the model instance.
   #  If this attribute was set to False (which is the default if not specified), the field
   #  would be required and the model instance would not be saved without a value for excerpt.
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
# self.likes is the ManyToManyField that holds the related User instances who have liked
# this post. It represents a set of User objects related to this particular post through
# the likes relationship. self.likes.count() calculates the total number of likes associated
# with this specific post. It returns the count of the related User instances, which
# corresponds to the number of likes.
# For example, if you have a Post instance called my_post, you can use this method to get
# the number of likes for that post like this: number_of_likes = my_post.number_of_likes()

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    # One To Many relationship - one post can have many comments
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment{self.body} by {self.name}"
