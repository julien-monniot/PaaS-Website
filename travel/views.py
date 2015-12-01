from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Travel


@login_required
def travel_list(request):
    travels = Travel.objects.order_by('created_date')
    return render(request, 'travel/travel_list.html', {'travels': travels})

@login_required
def travel_detail(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    return render(request, 'travel/travel_detail.html', {'travel': travel})

@login_required
def create_travel(request):
    html = "<html><body>Here there will be a form used to create a new travel</body></html>"
    return HttpResponse(html)
