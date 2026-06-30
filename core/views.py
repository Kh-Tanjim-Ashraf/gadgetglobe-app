from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def homePage(request):
    return render(request, template_name='homepage.html')


@login_required
def secretPage(request):
    return render(request, template_name='secret.html')