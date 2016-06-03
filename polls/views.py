from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
from polls.models import Poll
from django.template import RequestContext, loader
def index(request):
	latest_polls = Poll.objects.order_by('-pub_date')[:4]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_polls': latest_polls,
		})
	return HttpResponse(template.render(context))
def detail(request, poll_id):
	return HttpResponse("You're looking at poll %s." % poll_id)
def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)
def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
