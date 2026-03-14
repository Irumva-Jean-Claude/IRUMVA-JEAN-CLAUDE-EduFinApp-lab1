from django.urls import path
from .views import (
    testing_view,
    TransactionListView,
    TransactionDetailView,
    CategoryListView,
    CategoryDetailView,
    BudgetListView,
    BudgetDetailView
)

app_name = "core"

urlpatterns = [
    path('testing/', testing_view, name='testing'),
    path('testing/<int:id>/', testing_view, name='testing-detail'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:id>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('budgets/', BudgetListView.as_view(), name='budget-list'),
    path('budgets/<int:id>/', BudgetDetailView.as_view(), name='budget-detail'),
]