from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
from polls.models import Poll
def index(request):
	latest_polls = Poll.objects.order_by('-pub_date')[:4]
	output = ', '.join([p.question for p in latest_polls])
	return HttpResponse(output)
def detail(request, poll_id):
	return HttpResponse("You're looking at poll %s." % poll_id)
def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)
def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
