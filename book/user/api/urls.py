
from rest_framework.routers import SimpleRouter

from .views import UserViewSet

app_name = "user_api"

router = SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = router.urls