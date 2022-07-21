from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login_student, name='login_student'),
    path('logout/', views.logout_student, name='logout_student'),
    path('search_for_books/', views.search_book, name='search_book'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)