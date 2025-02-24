from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser
from django import forms
import re

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs=
            {'class':'form-control', 'placeholder':'E-mail'}))
    
    class Meta: 
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if not re.search(r'[A-Z]', password):
            raise ValidationError("A senha deve conter pelo menos uma letra maiúscula.")
        
        if not re.search(r'\d', password):
            raise ValidationError("A senha deve conter pelo menos um número.")
        
        if not re.search(r'[\W_]', password):
            raise ValidationError("A senha deve conter pelo menos um caractere especial (como @, #, $, etc.).")

        return password

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '''
        <ul class="form-text text-muted small">
            <li>Sua senha deve conter pelo menos 8 caracteres.</li>
            <li>Sua senha deve conter pelo menos 1 caractere especial, 1 número e 1 letra maiúscula.</li>
        </ul>
        
        '''
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '''
        <span class="form-text text-muted">
            <small>Digite a mesma senha de antes, para verificação.</small>
        </span>
        '''
