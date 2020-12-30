from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Show, Spent
from .forms import ShowForm, SpentForm


def index(request):
    return render(request, 'cash/index.html')


def about(request):
    return render(request, 'cash/about.html')


@login_required
def shows(request):
    show_name = Show.objects.filter(owner=request.user).order_by('date_added')
    context = {'show_name': show_name}
    return render(request, 'cash/shows.html', context)


@login_required
def show(request, show_id):
    show_name = Show.objects.get(id=show_id)
    if show_name.owner != request.user:
        raise Http404

    spent = show_name.spent_set.order_by('-date_added')
    context = {'show_name': show_name, 'spent': spent}
    return render(request, 'cash/show.html', context)


@login_required
def new_show(request):
    if request.method != 'POST':
        form = ShowForm()
    else:
        form = ShowForm(data=request.POST)
        if form.is_valid():
            new_show_name = form.save(commit=False)
            new_show_name.owner = request.user
            new_show_name.save()
            return redirect('cash:shows')

    context = {'form': form}
    return render(request, 'cash/new_show.html', context)


@login_required
def new_spent(request, show_id):
    show_name = Show.objects.get(id=show_id)

    if request.method != 'POST':
        form = SpentForm()
    else:
        form = SpentForm(data=request.POST)
        if form.is_valid():
            new_amount = form.save(commit=False)
            new_amount.show = show_name
            new_amount.save()
            return redirect('cash:show', show_id=show_id)

    context = {'show_name': show_name, 'form': form}
    return render(request, 'cash/new_spent.html', context)


@login_required
def edit_spent(request, spent_id):
    spent = Spent.objects.get(id=spent_id)
    show_name = spent.show
    if show_name.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = SpentForm(instance=spent)
    else:
        # POST data submitted; process data.
        form = SpentForm(instance=spent, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cash:show', show_id=show_name.id)

    context = {'spent': spent, 'show_name': show_name, 'form': form}
    return render(request, 'cash/edit_spent.html', context)
