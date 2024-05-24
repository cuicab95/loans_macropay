from rest_framework import routers
from . import views

app_name = "menu"
router = routers.SimpleRouter()
router.register("create", views.MenuViewSet)
urlpatterns = router.urls