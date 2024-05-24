from rest_framework import routers
from . import views

app_name = "customer"
router = routers.SimpleRouter()
router.register("process-payments", views.ProcessPaymentViewSet)
urlpatterns = router.urls