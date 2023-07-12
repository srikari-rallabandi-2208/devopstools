from django.urls import path
from devopstools.views import save_top_results

urlpatterns = [
    path('api/save-top-results/', save_top_results, name='save_top_results'),
]
