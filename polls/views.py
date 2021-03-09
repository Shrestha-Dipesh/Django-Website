from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice

def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question,'error_message': "Please select a choice!!!"})
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:result', args = (question.id,)))
