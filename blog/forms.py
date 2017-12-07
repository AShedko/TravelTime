from django import forms
from .models import Profile
from .models import Post
from django.contrib.auth.models import User
from django.forms import widgets

#class beautyWidget(widgets.TextInput):
    #def render(self, name, value, attrs=None):
        #return mark_safe(u'''<span>USD</span>%s''' % (super(beautyWidget, self).render(name, value, attrs)))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		class Meta:
			widgets = {
            'location': forms.TextInput(attrs={'class': "form-control"}), # or whatever class you want to apply
            # and so on
			}
		fields = ('location','birth_date','travel_groups')
		
		
