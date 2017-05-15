# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

from eim.forms import OldKcsForm, UnitForm, OperationForm
from eim.models import OldKcs, Unit, Operation, NewKcs, Component


def home(request):
    return render(request, 'eim/home.html')


def main_page(request):
    return render(request, 'index.html')


def OldKcsList(request):
    query = request.GET.get('q')
    obj_list = OldKcs.objects.all().order_by('-receive_date')

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
    form = OldKcsForm(request.POST)
    if request.method == 'POST':
        # if not request.user.is_staff or not request.user.is_superuser:
        #     raise Http404

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # message success
            messages.success(request, "Successfully Created")
        return redirect('receive_kcs')
    else:
        context = {
            "form": form,
        }
        return render(request, 'eim/oldkcs_create.html', context)


def UnitList(request):
    query = request.GET.get('q')
    obj_list = Unit.objects.all().order_by('new_kcs_number')

    if query:
        obj_list = obj_list.filter(
            Q(serial_number__icontains=query)
        ).distinct()

    context = {
        'UnitList': obj_list,
    }
    return render(request, "eim/unit_list.html", context)


def UnitCreate(request):
    form = UnitForm(request.POST)
    if request.method == 'POST':
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # message success
            messages.success(request, "Successfully Created")
        return redirect('unit_list')
    else:
        context = {
            "form": form,
        }
        return render(request, 'eim/unit_create.html', context)


def UnitDetail(request, id=None):
    if id is None:
        raise Http404
    obj = Unit.objects.get(id__exact=id)

    obj_operation = Operation.objects.filter(
        Q(target__exact=obj.serial_number)
        )

    context = {
        'unit': obj,
        'operations': obj_operation,
    }
    return render(request, "eim/unit_detail.html", context)

def OperationList(request):
    obj_list = Operation.objects.all().order_by("-time")
    print obj_list
    context = {
        'operation_list': obj_list,

    }
    return render(request, 'eim/operation_list.html', context)


def OperationDetail(request, id=None):
    if id is None:
        raise Http404
    obj = Operation.objects.get(id__exact=id)
    context = {
        'operation': obj,
    }
    return render(request, "eim/operation_detail.html", context)


def OperationCreate(request):
    form = OperationForm(request.POST)
    if request.method == 'POST':
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # message success
            messages.success(request, "Successfully Created")
        return redirect('operation_list')

    active_list = []

    get_active_instance = OldKcs.objects.active()
    for obj in get_active_instance:
        active_list.append(obj.kcs_number)

    get_active_instance = Unit.objects.active()
    for obj in get_active_instance:
        active_list.append(obj.serial_number)

    get_active_instance = NewKcs.objects.active()
    for obj in get_active_instance:
        active_list.append(obj.kcs_number)

    context = {
        'form': form,
        'active_list': active_list
    }
    return render(request, 'eim/operation_create.html', context)


def TergetValidation(request):

    return True


def ShowInventory(request):
    component_list = Component.objects.all()
    for component in component_list:
        component.total = component.eim_balance+ component.kam_balance

    context = {
        'component_list': component_list,
    }
    return render(request, 'eim/inventory.html', context)


def InventoryTransactionDetail(request):
    # TODO: add transaction view
    pass