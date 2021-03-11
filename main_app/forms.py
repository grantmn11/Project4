from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'date']

class UpdateCommentForm (ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'date']