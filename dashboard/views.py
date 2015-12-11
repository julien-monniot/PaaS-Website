from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Historique


@login_required
def main_panel(request):
    return render(request, 'dashboard/dashboard.html', {"historique":Historique.objects.all().order_by('-date')})
