from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

# View to handle new user registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Automatically log them in
            return redirect('tour_list')  # Redirect to homepage
    else:
        form = RegisterForm()
    
    return render(request, 'hiking_users/register.html', {'form': form})
