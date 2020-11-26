from django.urls import path
from .  import views

urlpatterns = [
    path('disponibilidad/<int:site_id>/<int:espacio_id>/<int:start_date>/<int:end_date>', views.disponibilidad, name='disponibilidad'),
]