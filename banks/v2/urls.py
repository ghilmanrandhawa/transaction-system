from django.urls import path

from banks.v2 import views

urlpatterns = [
    path('banks/', views.BankAPI.as_view(), name='bank_listing'),
    path('bank-details/<int:bank_id>/', views.BankDetailsAPI.as_view(), name='bank_details'),
    path('bank-branches/<int:bank_id>/', views.BranchAPI.as_view(), name='branch_listing'),
    path('branch-details/<int:branch_id>/', views.BranchDetailsAPI.as_view(), name='branch_listing'),
    path('branch-accounts/<int:branch_id>/', views.AccountAPI.as_view(), name='account_listing'),
    path('account-details/<int:acoount_id>/', views.AccountDetailsAPI.as_view(), name='account_details'),
    path('make-transaction/<int:account_id>/', views.TransactionAPI.as_view(), name='transaction_listing'),
    path('transaction-details/<int:transaction_id>/', views.TransactionDetailsAPI.as_view(), name='transaction_details'),

]
