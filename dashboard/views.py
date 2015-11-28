from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def main_panel(request):
    html = "<html><body>Main dashboard where users will get access to any website functionality" \
           "<br><a href='/users/logout/'>Logout</a></body></html>"
    return HttpResponse(html)