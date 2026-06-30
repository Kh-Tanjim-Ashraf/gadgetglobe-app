from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # Redirect authenticated user to dashboard
    if request.user.is_authenticated:
        return redirect('secretPage')
    
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, template_name='authentication/register.html', context=context)
