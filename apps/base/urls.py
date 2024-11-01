from rest_framework .routers import DefaultRouter
from .views import TaskAPI
router = DefaultRouter()
router.register('TASK', TaskAPI, basename = "task API")

urlpatterns = [

]

urlpatterns += router.urls