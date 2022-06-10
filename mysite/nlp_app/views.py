from datetime import timedelta
from string import punctuation
from django.urls import reverse
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
import numpy as np
import os



def IndexView(request):
    """Return the last five published questions."""
    name = "Manu"
    return render(request, 'nlp_app/home.html', {"name":name}) 