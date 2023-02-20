from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .forms import ReviewsForm
from .models import Reviews


def add_a_review(request):
    form = ReviewsForm()
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            comment = Reviews(
                name=form.cleaned_data["name"],
                review=form.cleaned_data["review"],
            )
            comment.save()

    context_form = {'form': form}

    return context_form


def return_feedback(request):
    form = add_a_review(request)
    reviews = Reviews.objects.all()
    paginator = Paginator(reviews, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'page': page, 'posts': posts, **form}

    return render(request, 'reviews.html', context)
