from django.shortcuts import render, get_object_or_404, redirect,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Travel
from wu.models import WuProfil
from .forms import TravelForm, StageFormSet
from .models import Stage
from .models import Participate
from dashboard.models import Historique
from django.views.generic import CreateView, UpdateView


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
def travel_detail(request, pk, message=""):
    travel = get_object_or_404(Travel, pk=pk)
    stages = Stage.objects.filter(travel=travel.id)
    participants = travel.participants.all()
    participating = False
    if len(travel.participants.filter(user=request.user.id)) > 0:
        participating = True
    return render(request, 'travel/travel_detail.html', {'message':message, 'travel': travel, 'stages':stages, 'participants':participants, 'participating':participating})

@login_required
def travel_subscribe(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    if len(travel.participants.filter(user_id=request.user.id)) < 1:
        participation=Participate(person=request.user.wuprofil, travel=travel, motivation=5)
        participation.save()

        Historique.newTravelFact(
            actor=request.user.wuprofil, 
            action_type="TS",
            object_travel=travel
        )


    return HttpResponseRedirect('/travel/%s/' % pk)


@login_required
def travel_unsubscribe(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    participations=Participate.objects.filter(person__user__id=request.user.id, travel_id=pk)
    if len(participations) > 0:
        for participation in participations:
            participation.delete()

        Historique.newTravelFact(
            actor=request.user.wuprofil, 
            action_type="TU",
            object_travel=travel
        )


    return HttpResponseRedirect('/travel/%s/' % pk)

'''
@login_required
def create_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST, request.FILES)

        if form.is_valid():
            print("Form valid")
            travel = form.save(commit=False)
            wu_user = WuProfil.objects.get(user=request.user)
            travel.author = wu_user
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
'''


@login_required
def create_travel(request):
    if request.POST:
        form = TravelForm(request.POST, request.FILES)

        if form.is_valid():
            print("Form valid")
            travel = form.save(commit=False)
            wu_user = WuProfil.objects.get(user=request.user)
            travel.author = wu_user
            stage_formset = StageFormSet(request.POST, instance=travel)
            if stage_formset.is_valid():
                travel.save()
                stage_formset.save()
                form.save_m2m()
                return travel_list(request)
            else :
                print("Stage formset invalid")
                print(form.errors)
        else :
            print("Travel formset invalid")
            print(form.errors)
    else:
        form = TravelForm()
        stage_formset = StageFormSet(instance=Travel())

    return render(request, "travel/add_travel.html", {"form": form, "stage_formset": stage_formset})


