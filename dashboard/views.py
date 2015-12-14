from django.shortcuts import render, HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Historique, Flow, Notification


@login_required
def main_panel(request):
    return render(request, 'dashboard/dashboard.html', 
		{
			"historique":Flow.objects.filter(Q(receiver__user__id=request.user.id)| Q(receiver__isnull=True)).order_by('-fact__date')
		}
	)
