from django.shortcuts import render, redirect
from django.views import View
from jarvisapp.forms import RecipeForm
# from jarvisapp.langchain import askJarvis
from jarvisapp.langchainactors import askBot

class Home(View):
    # def get(self, request):
    #     form = RecipeForm()
    #     ai_response = request.session.get('ai_response', '')
    #     # print(' got the ai_response : ', ai_response)
    #     return render(request, 'jarvisapp/home.html', {'form': form, 'ai_response': ai_response})

    # def post(self, request):
    #     form = RecipeForm(request.POST)
    #     if form.is_valid():
    #         user_prompt = form.cleaned_data['user_prompt']
    #         model_type = form.cleaned_data['model_type']
    #         ai_response = askBot(user_prompt, model_type)
    #         request.session['ai_response'] = ai_response
    #     form = RecipeForm()
    #     return redirect('/')

    def get(self, request):
        form = RecipeForm()
        ai_response = request.session.get('ai_response', '')
        user_prompt = request.session.get('user_prompt', '')
        
        if ai_response:
            del request.session['ai_response']
        
        if user_prompt:
            del request.session['user_prompt']
        
        return render(request, 'jarvisapp/home.html', {'form': form, 'ai_response': ai_response, 'user_prompt': user_prompt})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            user_prompt = form.cleaned_data['user_prompt']
            ai_response = askBot(user_prompt)
            request.session['user_prompt'] = user_prompt
            request.session['ai_response'] = ai_response

        form = RecipeForm()
        return redirect('/')