from django import forms
from models import Article

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
    
class ArticleForm(forms.ModelForm):
        
        class Meta:
            model= Article
            fields = ('thumbnail','title','body','pub_date')
            
#class CommentForm(forms.ModelForm):
    
    #class Meta:
       # model = Comment
        #fields = ('name','body')
        
