from django import forms

class ChatForm(forms.Form):
    MODEL_CHOICES = [
        ('openai', 'OpenAI'),
        ('anthropic', 'Anthropic'),
    ]
    user_prompt = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Write your prompt here...'}))
    model_type = forms.ChoiceField(choices=MODEL_CHOICES, widget=forms.Select(attrs={'placeholder': 'Select Model'}))
    