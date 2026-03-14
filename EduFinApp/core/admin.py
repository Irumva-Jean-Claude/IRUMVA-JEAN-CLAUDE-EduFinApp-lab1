from django.contrib import admin
from .models import Testing, Transaction, Category, Budget

admin.site.register(Testing)
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Budget)