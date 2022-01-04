from django.urls import path

from banks.v3 import views

urlpatterns = [
    path('banks/', views.BankListCreateAPI.as_view(), name='bank_listing'),
    path('bank-details/<int:pk>/', views.BankUpdateDeleteApi.as_view(), name='bank_details'),
    path('account-details/<int:pk>/', views.AccountUpdateDeleteAPI.as_view(), name='account_details'),
    path('transactions/', views.TransactionsListCreateApi.as_view(), name='transaction_list'),

    ]
