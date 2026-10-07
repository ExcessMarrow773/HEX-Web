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

def mission(request):
    if str(request.user) == "AnonymousUser":
        context = {
            "security_level": 0,
            "security_access": "Guest"
        }
        return render(request, "app/guest_mission.html", context)
        
    else:
        account = User.objects.get(pk=request.user.pk)
        profile = account.profile
        security_level = profile.security_level()
        security_access = int(profile.security_access)
        context = {
            "account": account,
            "profile": profile,
            "security_level": security_level,
            "security_access": security_access
        }
        
        if security_access >= 2:
            return render(request, "app/mission.html", context)
        else:
            return render(request, "app/guest_mission.html", context)