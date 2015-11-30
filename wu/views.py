from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from .models import WuProfil
from django.contrib.auth.models import User

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'index.html', {})
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return redirect('/dashboard')


# TODO : change this to class with post method
def register(request):

    # Used later if registration is valid
    registered = False

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # create regular user in database + set password
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # commit= false delays the transaction for WuProfil
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'wu/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your WUP account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'wu/login.html', {})


def user_logout(request):
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        username = request.user.username
        return logout_then_login(request, '/users/login', {'username': username})


def user_profile(request):
    wu_user = get_object_or_404(WuProfil, user=request.user)
    return render(request, 'wu/profile.html', { 'user': request.user, 'wu_user': wu_user })

# problem here !
def user_list(request):
    current_user = request.user
    users = User.objects.all()
    users = users.exclude(username=current_user.username)
    wu_users = WuProfil.objects.all()
    wu_users = wu_users.exlude(username=current_user.username)
    return render(request, 'wu/wu_list.html', { 'users': users, 'wu_users': wu_users })

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    wu_user = WuProfil.objects.get(user = user)
    return render(request, 'wu/wu_list.html', { 'user': user, 'wu_user': wu_user })