from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet)
router.register("products", views.ProductViewSet)

urlpatterns = router.urls
