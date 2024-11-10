from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PredictAPIView, PredictPlantDisease

urlpatterns = [
    path('predict', PredictAPIView.as_view()),
    path("plant-disease", PredictPlantDisease.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)