from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Travel
from .models import Stage
from .models import Participate

@login_required
def travel_list(request):
    travels = Travel.objects.order_by('created_date')
    return render(request, 'travel/travel_list.html', {'title':'Liste des voyages', 'travels': travels})

@login_required
def my_created_travels(request):
	travels = Travel.objects.filter(author__user=request.user.id).order_by('created_date')
	return render(request, 'travel/travel_list.html', {'title':'Mes voyages créés', 'travels': travels})

@login_required
def my_travels(request):
    travels = Travel.objects.filter(id__in=[participate.travel.id for participate in Participate.objects.filter(person__user=request.user.id)]).order_by('created_date')
    return render(request, 'travel/travel_list.html', {'title':'Mes voyages', 'travels': travels})

@login_required
def travel_detail(request, pk, message=""):
    travel = get_object_or_404(Travel, pk=pk)
    stages = Stage.objects.filter(travel=travel.id)
    participants = travel.participants.all()
    participating = False
    if len(travel.participants.filter(user=request.user.id)) > 0:
        participating = True
    return render(request, 'travel/travel_detail.html', {'message':message, 'travel': travel, 'stages':stages, 'participants':participants, 'participating':participating})

@login_required
def travel_subscribe(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    if len(travel.participants.filter(user_id=request.user.id)) < 1:
        participation=Participate(person=request.user.wuprofil, travel=travel, motivation=5)
        participation.save()

    return HttpResponseRedirect('/travel/%s/' % pk)


@login_required
def travel_unsubscribe(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    participations=Participate.objects.filter(person__user__id=request.user.id, travel_id=pk)
    if len(participations) > 0:
        for participation in participations:
            participation.delete()
     

    return HttpResponseRedirect('/travel/%s/' % pk)

@login_required
def create_travel(request):
    html = "<html><body>Here there will be a form used to create a new travel</body></html>"
    return HttpResponse(html)
