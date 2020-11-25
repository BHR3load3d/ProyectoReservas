from django.urls import path
from .  import views

urlpatterns = [
    path('disponibilidad/<int:tipo>/<int:site_id>/<int:start_date>/<int:end_date>', views.disponibilidad, name='disponibilidad'),
]