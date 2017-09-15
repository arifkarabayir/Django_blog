from django.forms import ModelForm
from .models import Post, Profile, Comment

#class PostForm(forms.Form):
#    class Meta:
    #title = forms.CharField(label='title', max_length=40)
    #text = forms.CharField(label='text', widget=forms.Textarea)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class LoginForm(ModelForm):
    class Meta:
        profile = Profile
        fields = ['username', 'password']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_owner', 'comment']
