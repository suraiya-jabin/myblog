from django.forms import ModelForm

from blog.models import Post
class blogForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'content' , 'pub_date','author']