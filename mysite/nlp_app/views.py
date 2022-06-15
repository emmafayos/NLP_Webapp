from datetime import timedelta
from string import punctuation
from django.urls import reverse
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
import numpy as np
import os
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect


def IndexView(request):
    """Return the last five published questions."""
    name = ["Manu", "Manu2"]
    return render(request, 'nlp_app/home.html', {"name":name})

def NLPView(request):
    title = request.POST["query1"]
    cosine_sim = pd.read_csv("nlp_app/data/cosine_sim.csv", index_col=0)
    books = pd.read_csv("nlp_app/data/full_books.csv", index_col=0)
    indices = pd.Series(books.index)

    recommended_books = []
    books_images = []
    title = title.lower()
    index = indices[indices == title].index[0]
    similarity_scores = pd.Series(cosine_sim.iloc[index,:]).sort_values(ascending = False)
    top_10_books = list(similarity_scores.iloc[1:12].index)
    top_10_scores = list(similarity_scores.iloc[1:12])
    for index, (i, score) in enumerate(zip(top_10_books,top_10_scores)):
        recommended_books.append([f"Recommendation {index}: {list(books.index)[int(i)]} - similarity score of {round(score,3)}"][0])
        books_images.append(books.iloc[int(i)]['thumbnail'])

    display_books = zip(recommended_books, books_images)

    return render(request, 'nlp_app/home.html', {'books':display_books})

