from typing import Any
from django.shortcuts import render, get_object_or_404
from . models import Question,Choice
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . forms import ExempleForm
from django.views import View





def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template_name = 'app_exemplo/index.html'
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, template_name, context)


def detail(request, question_id):
    template_name = 'app_exemplo/details.html'
    question = get_object_or_404(Question, pk=question_id)
    return render(request, template_name, {'question': question})

class Form(View):
    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        super().setup(request, *args, **kwargs)
        self.contexto={
            'form':ExempleForm()
        }
        template_name = 'app_exemplo/form.html'
        self.pagina = render(request,template_name,self.contexto)
    
    def get(self, *args, **kwargs):
        return self.pagina
    
    def post(self, *args, **kwargs):
        formulario = ExempleForm(self.request.POST)
        if formulario.is_valid():
            formulario.save()
            
        return self.pagina
        
    
