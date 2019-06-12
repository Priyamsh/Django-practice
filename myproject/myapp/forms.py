from django import forms
from myapp.models import Reporter,User,Profile

class Loginform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password']
        
    def clean_username(self):
        username=self.cleaned_data.get('username')
        articleuser=Reporter.objects.filter(name=username)
        print(articleuser)
        if (articleuser.count==0):
            raise forms.ValidationError("Not a Reporter")
        return username
    
class ProfileForm(forms.ModelForm):
    name=forms.CharField(max_length=50)
    picture=forms.ImageField()
    class Meta:
        model=Profile
        fields=['name','picture']