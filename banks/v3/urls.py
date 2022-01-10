from django.urls import path

from banks.v3 import views

urlpatterns = [
    path('banks/', views.BankListCreateAPI.as_view(), name='bank_listing'),
    path('bank/<int:pk>/', views.BankUpdateDeleteAPI.as_view(), name='bank_details'),
    path('bank/<int:pk>/branches/', views.BranchListCreateAPI.as_view(), name='branch_list'),
    path('branch/<int:pk>/', views.BranchUpdateDeleteAPI.as_view(), name='branch_details'),
    path('branch/<int:pk>/accounts/', views.AccountListCreateAPI.as_view(), name='account_details'),
    path('account/<int:pk>/', views.AccountUpdateDeleteAPI.as_view(), name='account_details'),
    path('account/<int:pk>/transactions/', views.TransactionsListCreateApi.as_view(), name='transaction_list'),
    path('transaction/<int:pk>/', views.TransactionDeleteAPI.as_view(), name='transaction_details'),
]
