# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.") 

from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render
from django.http import Http404 

def detail(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/detail.html',{'question':question})





def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html',context)
 


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    reponse = "You're lookign at the results of question %s."
    return HttpResponse(reponse % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

