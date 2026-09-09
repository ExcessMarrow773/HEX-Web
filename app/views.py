from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Q

from app.models import Post

from itertools import chain
from operator import attrgetter
from datetime import timedelta

from accounts.models import CustomUser

import os
import json

User = get_user_model()
# Create your views here.


# Create your views here.

def index(request):
    context = {
        'account': CustomUser.objects.all()
    }
    return render(request, "app/index.html", context)

def staff(request):
    context = {
        "staff_accounts": CustomUser.objects.filter(goes_on_staff_page=True)
    }

    return render(request, "app/staff.html", context)