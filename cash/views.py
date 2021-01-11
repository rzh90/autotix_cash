from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from autoslug import AutoSlugField
# from django.urls import reverse

from .forms import ShowForm, SpentForm, DeleteSpentForm, DeleteShowForm
from .models import Show, Spent


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
def show(request, slug):
    show_name = get_object_or_404(Show, slug=slug)
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
def new_spent(request, slug):
    show_name = Show.objects.get(slug=slug)

    if request.method != 'POST':
        form = SpentForm()
    else:
        form = SpentForm(data=request.POST)
        if form.is_valid():
            new_amount = form.save(commit=False)
            new_amount.show = show_name
            new_amount.save()
            return redirect('cash:show', slug=slug)

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
            return redirect('cash:show', slug=show_name.slug)

    context = {'spent': spent, 'show_name': show_name, 'form': form}
    return render(request, 'cash/edit_spent.html', context)


@login_required
def delete_spent(request, spent_id):
    spent = get_object_or_404(Spent, id=spent_id)
    show_name = spent.show

    if show_name.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = DeleteSpentForm(request.POST, instance=spent)
        if form.is_valid():
            spent.delete()
            return redirect('cash:show', slug=show_name.slug)
            # return HttpResponseRedirect('cash/index.html')
    else:
        form = DeleteSpentForm(instance=spent)

    context = {'spent': spent, 'show_name': show_name, 'form': form}
    return render(request, 'cash/delete_spent.html', context)


def delete_show(request, slug):
    show_name = Show.objects.get(slug=slug)

    if show_name.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = DeleteShowForm(request.POST, instance=show_name)
        if form.is_valid():
            show_name.delete()
            return redirect('cash:shows')
    else:
        form = DeleteShowForm(instance=show_name)

    context = {'show_name': show_name, 'form': form}
    return render(request, 'cash/delete_show.html', context)


"""@login_required
def delete_spent(request, spent_id):
    spent = Spent.objects.get(id=spent_id)
    show_name = spent.show
    if show_name.owner != request.user:
        raise Http404
    else:
        spent.delete()
        return HttpResponseRedirect(reverse('cash:show', args = [show_name.id]))"""
