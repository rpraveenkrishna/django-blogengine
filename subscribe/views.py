from django.template import RequestContext
from django.shortcuts import render_to_response
from subscribe.forms import SubscriberForm
from subscribe.models import Subscriber
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'GET':
        subscriber_form = SubscriberForm()
    else:
        subscriber_form = SubscriberForm(request.POST)
        
        if subscriber_form.is_valid():
            data = subscriber_form.cleaned_data
            try:
                subscriber_exists = Subscriber.objects.get(email = data['email'])
            except Subscriber.DoesNotExist:
                subscriber_exists = None
                

            if subscriber_exists:
                subscriber_form = SubscriberForm(request.POST, instance = subscriber_exists)
                subscriber_form.save()
                return HttpResponseRedirect('/subscribe/subscribed-already/')
            else:
                subscriber_form.save()
                return HttpResponseRedirect('/subscribe/thanks/')
                

    return render_to_response(
    'subscribe/index.html', 
    {
    'form': subscriber_form
    }, 
    context_instance=RequestContext(request))
    
    

def thanks(request):
    if request.method == 'GET':
            
        return render_to_response('subscribe/index.html',{'thanks' : True}, 
        context_instance=RequestContext(request))
        

def subscribed_already(request):
    if request.method == 'GET':
        return render_to_response('subscribe/index.html',{'subscribed_already' : True}, 
        context_instance=RequestContext(request))

        
