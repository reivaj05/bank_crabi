from rest_framework import routers
from .views import (
    AccountsViewSet, TransactionsViewSet, AuthorizationsViewSet,
    CapturesViewSet, DepositsViewSet, UsersViewSet, TransfersViewSet
)

router = routers.SimpleRouter()

router.register(r'accounts', AccountsViewSet)
router.register(r'transactions', TransactionsViewSet)
router.register(r'authorizations', AuthorizationsViewSet)
router.register(r'captures', CapturesViewSet)
router.register(r'deposits', DepositsViewSet)
router.register(r'transfers', TransfersViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = router.urls
