from django.urls import path

from banks.v5 import views

urlpatterns = [
    path('banks/', views.BankAPI.as_view({'get': 'list', 'post': 'create'}), name='bank_listing'),
    path('bank/<int:pk>/', views.BankAPI.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'}), name='bank_details'),
    path('bank/<int:pk>/branches/', views.BranchAPI.as_view({'get': 'list', 'post': 'create'}), name='branch_listing'),
    path('branch/<int:pk>/', views.BranchAPI.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='branch_details'),
    path('branch/<int:pk>/accounts/', views.AccountAPI.as_view({'get': 'list'}), name='account_listing'),
    path('account/<int:pk>/', views.AccountAPI.as_view({'get': 'retrieve',
                                                        'put': 'update',
                                                        'delete': 'destroy'}), name='account_details'),
    path('account/<int:pk>/transactions/', views.TransactionAPI.as_view({'get': 'list', 'post': 'create'}), name='transactions_list'),
    path('transaction/<int:pk>/', views.TransactionAPI.as_view({'get': 'retrieve',
                                                                'delete': 'destroy'}), name='transaction_details'),
]
