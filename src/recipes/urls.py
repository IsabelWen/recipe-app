from django.urls import path
from .views import home
from .views import RecipesListView, RecipesDetailView, RecipesAuthorView

app_name = 'recipes'  

urlpatterns = [
   path('', home, name='home'),
   path('recipes/', RecipesListView.as_view(), name='recipes'),
   path('recipes/<int:pk>', RecipesDetailView.as_view(), name='detail'),
   path('recipes/author/<int:pk>/', RecipesAuthorView.as_view(), name='author'),
]
