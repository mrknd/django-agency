from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import BlogPost, Case, Contacts
from bs4 import BeautifulSoup


def home(request):
    return render(request, 'home.html')


def about_us_page(request):
    return render(request, 'about_us.html')


def services_page(request):
    return render(request, 'services.html')


def cases_page(request):
    cases = Case.objects.filter(is_published=True)
    return render(request, 'cases.html', {'cases': cases})


def career_page(request):
    return render(request, 'career.html')
    

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
    category = request.GET.get('category')

    posts = BlogPost.objects.filter(is_published=True)

    if category and category != 'all':
        posts = posts.filter(category=category)

    context = {
        'posts': posts,
        'current_category': category or 'all'
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    top_posts = BlogPost.objects.filter(is_published=True).exclude(pk=post.pk)[:3]

    soup = BeautifulSoup(post.content, 'html.parser')
    toc = []
    used_ids = set()

    for index, heading in enumerate(soup.find_all('h2'), start=1):
        heading_text = heading.get_text(strip=True)

        if not heading_text:
            continue

        base_id = slugify(heading_text) or f'section-{index}'
        unique_id = base_id
        counter = 1

        while unique_id in used_ids:
            unique_id = f'{base_id}-{counter}'
            counter += 1

        used_ids.add(unique_id)
        heading['id'] = unique_id

        toc.append({
            'id': unique_id,
            'title': heading_text,
        })

    processed_content = str(soup)

    context = {
        'post': post,
        'top_posts': top_posts,
        'toc': toc,
        'processed_content': processed_content,
    }
    return render(request, 'blog_detail.html', context)


def contacts_page(request):
    contacts = Contacts.objects.first()
    return render(request, 'contacts.html', {
        'contacts': contacts
    })