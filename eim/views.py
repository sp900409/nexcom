# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from eim.forms import OldKcsForm
from eim.models import OldKcs


def home(request):
    return render(request, 'eim/home.html')


def mainpage(request):
    return render(request, 'index.html')



def OldKcsList(request):
    query = request.GET.get('q')
    obj_list = OldKcs.objects.all()

    if query:
        obj_list = obj_list.filter(
                Q(kcs_number__icontains=query)
        ).distinct()

    # TODO: revise paginator here
    # paginator = Paginator(obj_list, 10)  # Show 10 contacts per page
    # page_request_var = "page"
    # page = request.GET.get(page_request_var)
    # try:
    #     obj_list = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     obj_list = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     obj_list = paginator.page(paginator.num_pages)

    context = {
        'OldKcsList': obj_list,
        # "page_request_var": page_request_var,
    }
    return render(request, "eim/oldkcs.html", context)


def OldKcsCreate(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404

    form = OldKcsForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect('eim/oldkcs.html')
    context = {
        "form": form,
    }
    return render(request, 'eim/oldkcs_create.html', context)
