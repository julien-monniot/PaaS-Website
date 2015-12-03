from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Travel
from .forms import TravelForm


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
    if request.method == 'POST':
        form = TravelForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #return travel_detail(request, )
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = TravelForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render('travel/add_travel.html', {'form': form})
