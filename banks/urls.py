from django.urls import path

from . import views

urlpatterns = [
    path('banks/', views.get_banks, name='bank_listing'),
    path('bank/<int:pk>/', views.get_bank_details, name='bank_details'),
    path('bank/create/', views.create_bank, name='add_bank'),
    path('bank-update/<int:pk>/', views.update_bank_details, name='update_bank'),
    path('bank-delete/<int:pk>/', views.delete_bank, name='delete_bank'),
    path('accounts/', views.get_accounts, name='account_listing'),
    path('account/<int:pk>/', views.get_account_details, name='account_details'),
    path('account-create', views.create_account, name='add_account'),
    path('account-update/<int:pk>/', views.update_account_details, name='update_account'),
    path('account-delete/<int:pk>/', views.delete_account, name='delete_account'),
    path('branchs/', views.get_branches, name='branch_listing'),
    path('branch/<int:pk>/', views.get_branch_details, name='branch_details'),
    path('branch-create/', views.create_branch, name='add_branch'),
    path('branch-update/<int:pk>/', views.update_branch_details, name='update_branch'),
    path('branch-delete/<int:pk>/', views.delete_branch, name='update_branch'),
    path('make-transaction/', views.make_transaction, name='make_transaction'),
    path('transactions/', views.get_transactions, name='transaction_list'),
]
