from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import DepartedMember, Tribute
from .forms import TributeForm

def tribute_list(request):
    departed_members = DepartedMember.objects.all()
    tributes = Tribute.objects.all().order_by('-created_at')
    return render(request, 'tributes/tribute_list.html', {
        'departed_members': departed_members,
        'tributes': tributes,
    })

@login_required
def create_tribute(request):
    if request.method == 'POST':
        form = TributeForm(request.POST)
        if form.is_valid():
            tribute = form.save(commit=False)
            tribute.author = request.user
            tribute.save()
            return redirect('tribute_list')
    else:
        form = TributeForm()
    
    return render(request, 'tributes/create_tribute.html', {
        'form': form,
    })