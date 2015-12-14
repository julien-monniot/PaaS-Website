from django.shortcuts import render, HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Historique, Flow, Notification
from django.core.exceptions import ObjectDoesNotExist

def get_notif_count(request):
	if not request.user.is_anonymous():
		try:
			count = Notification.objects.filter(receiver=request.user.wuprofil, seen=False).count()
			has_notifs = False
			if count > 0:
				has_notifs = True
			return {"notif_count":Notification.objects.filter(receiver=request.user.wuprofil, seen=False).count(),
					"has_notifs":has_notifs
					}
		except ObjectDoesNotExist:
			return {"notif_count":0,
					"has_notifs":False
					} 
	return {}