from django.urls import path

from . import views

urlpatterns = [
    path('banks/list', views.banks_listing, name='bank-listing'),
    path('bank/details/<int:pk>', views.get_bank_details, name='bank-details'),
    path('bank/create', views.create_bank, name='add-bank'),
    path('bank/update/<int:pk>', views.update_bank_details, name='update-bank'),
    path('bank/delete/<int:pk>', views.delete_bank, name='delete-bank'),
    path('acount/list', views.account_listing, name='account-listing'),
    path('account/details/<int:pk>', views.get_account_details, name='account-details'),
    path('account/create', views.create_account, name='add-account'),
    path('account/update/<int:pk>', views.update_account_details, name='update-account'),
    path('account/delete/<int:pk>', views.delete_account, name='delete-account'),
    path('branch/list', views.branch_listing, name='branch-listing'),
    path('branch/details/<int:pk>', views.get_branch_details, name='branch-details'),
    path('branch/create', views.create_branch, name='add-branch'),
    path('branch/update/<int:pk>', views.update_branch_details, name='update-branch'),
    path('branch/delete/<int:pk>', views.delete_branch, name='update-branch'),
]
