from django.shortcuts import render, get_object_or_404
from . models import Question,Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse




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


