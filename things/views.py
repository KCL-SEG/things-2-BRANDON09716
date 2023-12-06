from django.shortcuts import render
from .forms import MyForm
def home(request):
    submitted = False
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            submitted = True
    else:
        form = MyForm()

    return render(request, 'home.html', {'form': form, 'submitted': submitted})