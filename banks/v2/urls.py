from django.urls import path

from banks.v2 import views

urlpatterns = [
    path('banks/', views.BankApi.as_view(), name='bank_listing'),
    path('bank-details/<int:bank_id>/', views.BankDetailsAPi.as_view(), name='bank_details'),
    path('bank-branches/<int:bank_id>/', views.BranchApi.as_view(), name='branch_listing'),
    path('branch-details/<int:branch_id>/', views.BranchDetailsApi.as_view(), name='branch_listing'),
    path('branch-accounts/<int:branch_id>/', views.AccountApi.as_view(), name='account_listing'),
    path('account-details/<int:acoount_id>/', views.AccountDetailsApi.as_view(), name='account_details'),
    path('make-transaction/<int:account_id>/', views.TransactionApi.as_view(), name='transaction_listing'),
    path('transaction-details/<int:transaction_id>/', views.TransactionDetailsApi.as_view(), name='transaction_details'),

]
