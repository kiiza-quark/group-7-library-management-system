from django.contrib import admin
from .models import Book,Student,IssuedBook

admin.site.site_header = "LIBRARY MANAGEMENT"
admin.site.site_title = "LIBRARIAN SITE"

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)
