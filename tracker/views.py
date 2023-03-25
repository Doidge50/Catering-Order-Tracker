from django.shortcuts import render, redirect
from tracker.forms import *
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from tracker.models import *
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from tracker.helpers.auth import error_403_if_not_mentioned_student_or_admin
from django.db.models import Sum
from tracker.decorators import *
import datetime
from datetime import timedelta
from collections import defaultdict
from dateutil.relativedelta import relativedelta
import calendar
import json


@login_required
def log_out(request):
    """
    Logs out the specified user
    """
    logout(request)
    return redirect('log_in')


@guest_user_required
def log_in(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.add_message(request, messages.ERROR, "Username and password combination do not match a valid user. Please try again.")
            else:
                login(request, user)
                return redirect('dashboard')
    form = LoginUserForm()
    return render(request, 'templates/log_in.html', {'form': form})

@login_required
@require_GET
def dashboard(request):
    user = request.user
    return render(request, 'templates/client/client_dashboard.html')



@login_required
def orders(request, user_id):
    error_403_if_not_mentioned_student_or_admin(request, User.objects.get(id = user_id))
    orders = Order.objects.filter(user = request.user).order_by('-timeOrdered')
    if request.method == 'POST':
        form = OrderForm(request.POST, cat_user = request.user)
        if form.is_valid():
            saved_form = form.save(False)
            saved_form.user = request.user
            saved_form.timeOrdered = datetime.datetime.today()
            saved_form.save()
            # this add_score line is for add score to each transaction records in a day and only one score for one day
            orders = Order.objects.filter(user = request.user).order_by('-date')
            return redirect('transactions', request.user.id)
        else:
            return render(request, 'templates/client/transactions.html', {'form': form, 'orders': orders})
    else:
        form = OrderForm(cat_user = request.user)
        return render(request, 'templates/client/transactions.html', {'form': form, 'orders': orders})
    