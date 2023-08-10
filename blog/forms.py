from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):

# The inner class Meta within the CommentForm class is used to provide metadata about the form. It tells Django how to create the form based on the Comments model.

# model = Comments: This line specifies the model that the form is based on. In this case, the model is Comments, which presumably represents the comments users can leave.

# fields = ('body',): This line specifies which fields from the model should be included in the form. Here, only the 'body' field is included. This suggests that the form is intended to capture the body or content of the comment.
    class Meta:
        model = Comment
        fields = ('body',)

