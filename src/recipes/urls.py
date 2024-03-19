from django.urls import path
from .views import home
from .views import RecipesListView, RecipesDetailView

app_name = 'recipes'  

urlpatterns = [
   path('', home),
   path('recipes/', RecipesListView.as_view(), name='recipes'),
   path('recipes/<pk>', RecipesDetailView.as_view(), name='detail'),
]
