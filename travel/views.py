from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Travel
from wu.models import WuProfil
from .forms import TravelForm
from .models import Stage
from .models import Participate

@login_required
def travel_list(request):
    travels = Travel.objects.order_by('-created_date')
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
    if request.method == 'POST':
        form = TravelForm(request.POST, request.FILES)

        if form.is_valid():
            print("Form valid")
            travel = form.save(commit=False)
            wu_user = WuProfil.objects.get(user=request.user)
            travel.author = wu_user
            #travel.participants = Participants.wu_user
            travel.save()
            form.save_m2m()
            return travel_list(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print("form invalid")
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = TravelForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'travel/add_travel.html', {'form': form})
