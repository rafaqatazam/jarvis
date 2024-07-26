import logging
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from jarvisapp.forms import ChatForm
from .langchain.bot import Bot

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Home(View):
    
    def get(self, request):
        form = ChatForm()
        ai_response = request.session.pop('ai_response', '')
        user_prompt = request.session.pop('user_prompt', '')
        
        context = {
            'form': form,
            'ai_response': ai_response,
            'user_prompt': user_prompt,
        }
        return render(request, 'jarvisapp/home.html', context)

    def post(self, request):
        form = ChatForm(request.POST)
        if form.is_valid():
            user_prompt = form.cleaned_data['user_prompt']
            model_type = form.cleaned_data['model_type']
            try:
                bot = Bot(model_type=model_type, agent_type='react')
                ai_response = bot.ask(user_prompt)
            except Exception as e:
                if hasattr(e, 'response') and e.response is not None:
                    error_details = e.response.json()
                    error_message = error_details.get('error', {}).get('message', 'No error message available')
                else:
                    error_message = str(e)
                logging.error(f'{error_message}')
                ai_response = error_message

            request.session['user_prompt'] = user_prompt
            request.session['ai_response'] = ai_response

        return redirect(reverse('home'))
