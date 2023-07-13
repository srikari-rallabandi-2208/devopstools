from django.urls import path
from devopstools.views import save_top_results, top_results

urlpatterns = [
    path('api/save-top-results/', save_top_results, name='save_top_results'),
    path('top-results/', top_results, name='top_results'),
]
