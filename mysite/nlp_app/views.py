from datetime import timedelta
from string import punctuation
from django.urls import reverse
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
import numpy as np
import os
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect


def IndexView(request):
    """Return the last five published questions."""
    name = ["Harry Potter and the Philosopher Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban"]
    return render(request, 'nlp_app/home.html', {"name":name})

def NLPView(request):
    test = 'test'
    return render(request, 'nlp_app/home.html', {'test':test})