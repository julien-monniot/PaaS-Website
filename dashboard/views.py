from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def main_panel(request):
    return render(request, 'dashboard/index.html')