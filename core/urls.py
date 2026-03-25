from django.urls import path
from django.conf.urls.static import static
from config import settings
from .views import blog_page, blog_detail, contacts_page, home, cases_page, about_us_page, services_page, case_detail, career_page

urlpatterns = [
    path('', home, name='home'),
    path('about_us/', about_us_page, name='about_us'),
    path('services/', services_page, name='services'),
    path('cases/', cases_page, name='cases'),
    path('contacts/', contacts_page, name='contacts'),
    path('career/', career_page, name='career'),
    path('cases/<slug:slug>/', case_detail, name='case_detail'),
    path('blog/', blog_page, name='blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)