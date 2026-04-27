from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Course

def home(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        try:
            rating = int(request.POST.get('rating'))
            if 1 <= rating <= 5:
                Course.objects.create(
                    course_name=course_name,
                    rating=rating
                )
        except (ValueError, TypeError):
            pass
        return redirect('/')

    courses = Course.objects.all().order_by('-id')
    avg_rating = courses.aggregate(Avg('rating'))['rating__avg'] or 0

    context = {
        'courses': courses,
        'avg_rating': avg_rating
    }

    return render(request, 'index.html', context)


def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('/')


def pdf(request):
    courses = Course.objects.all()
    avg_rating = courses.aggregate(Avg('rating'))['rating__avg'] or 0

    context = {
        'courses': courses,
        'avg_rating': avg_rating
    }

    return render(request, 'pdf.html', context)