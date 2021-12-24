from django.urls import path

from banks.v1 import views

urlpatterns = [
    path('banks/', views.BankGetCreateApi.as_view(), name='bank_listing'),
    path('bank/<int:pk>/', views.BankUpdateDeleteApi.as_view(), name='bank_details'),
    path('accounts/', views.AccountGetCreateApi.as_view(), name='account_listing'),
    path('account/<int:pk>/', views.AccountUpdateDeleteApi.as_view(), name='account_details'),
    path('branchs/', views.BankGetCreateApi.as_view(), name='branch_listing'),
    path('branch/<int:pk>/', views.BranchUpdateDeleteApi.as_view(), name='branch_details'),
    path('transactions/', views.TransactionsGetCreateApi.as_view(), name='transaction_list'),
    path('transaction/<int:pk>/', views.TransactionsDeleteRetrieveApi.as_view(), name='transaction_list'),
]
