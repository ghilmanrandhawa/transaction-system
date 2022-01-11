from django.urls import path, include
from rest_framework.routers import DefaultRouter

from banks.v5 import views

router = DefaultRouter()

router.register('banks', views.BankAPI, basename='banks')
router.register(r'bank/(?P<bank_id>[^/.]+)/branches', views.BranchAPI, basename='branches')
router.register('branch/(?P<branch_id>[^/.]+)/accounts', views.AccountAPI, basename='accounts')
router.register('account/(?P<account_id>[^/.]+)/transactions', views.TransactionAPI, basename='accounts')

urlpatterns = [
    path('', include(router.urls)),
    ]
