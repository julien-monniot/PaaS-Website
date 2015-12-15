from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Historique, Flow, Notification


@login_required
def main_panel(request):
    return render(request, 'dashboard/dashboard.html', 
		{
			"title":"Bienvenue","historique":Flow.objects.filter(Q(receiver__user__id=request.user.id)| Q(receiver__isnull=True)).order_by('-fact__date')
		}
	)
@login_required
def notifications(request):
	return render(request, 'dashboard/notifications.html', 
		{
			"title":"Vos Notifications","notifications":Notification.objects.filter(Q(receiver__user__id=request.user.id)| Q(receiver__isnull=True)).order_by('-id')
		}
	)

@login_required
def notification_link(request, pk):
	notif = get_object_or_404(Notification, pk=pk)
	notif.seen = True
	notif.save()
	return render(request, 'dashboard/dashboard.html', 
		{
			"historique":Flow.objects.filter(fact__id=notif.fact.id)
		}
	)
