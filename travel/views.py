from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def travel_list(request):
    html = "<html><body>Travel List here</body></html>"
    return HttpResponse(html)

@login_required
def travel_detail(request, pk):
    html = "<html><body>Details for a trip here</body></html>"
    return HttpResponse(html)

@login_required
def create_travel(request):
    html = "<html><body>Here there will be a form used to create a new travel</body></html>"
    return HttpResponse(html)