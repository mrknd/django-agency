from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Case


def home(request):
    return render(request, 'home.html')


def about_us_page(request):
    return render(request, 'about_us.html')


def services_page(request):
    return render(request, 'services.html')


def cases_page(request):
    cases = Case.objects.filter(is_published=True)
    return render(request, 'cases.html', {'cases': cases})
    

def case_detail(request, slug):
    case = get_object_or_404(Case, slug=slug, is_published=True)
    related_cases = Case.objects.filter(is_published=True).exclude(id=case.id)[:2]
    return render(request, 'case-detail.html', {
        'case': case,
        'related_cases': related_cases,
    })


def contacts_page(request):
    return render(request, 'contacts.html')



def blog_page(request):
    return render(request, 'blog.html')


def blog_detail(request):
    return render(request, 'blog-detail.html')