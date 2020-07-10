from django import forms
from .models import *

class TodoForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TodoForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs['style'] = "width:55rem"
    title = forms.CharField(widget=forms.TextInput(attrs={
         'size' :'120',
         'placeholder' : 'أضف مهامك هنا'
        }))
    class Meta:
        model = Todo
        fields = ("title",)

class Update_TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ("title",)