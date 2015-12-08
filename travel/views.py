from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
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
def travel_detail(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    stages = Stage.objects.filter(travel=travel.id)
    participants = travel.participants.all()
    return render(request, 'travel/travel_detail.html', {'travel': travel, 'stages':stages, 'participants':participants})

@login_required
def create_travel(request):
    html = "<html><body>Here there will be a form used to create a new travel</body></html>"
    return HttpResponse(html)
