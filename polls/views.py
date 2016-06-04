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
	#context = {'latest_polls': latest_polls}
	#return render(request, 'polls/index.html', context)
def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	#poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html',{'poll': poll})
def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)
def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
