from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import RecipesListView, RecipesDetailView, RecipesAuthorView, create_recipe, update_recipe, delete_recipe, about

app_name = 'recipes'  

urlpatterns = [
   path('', home, name='home'),
   path('aboutme/', about, name='about'),
   path('recipes/', RecipesListView.as_view(), name='recipes'),
   path('recipes/<int:pk>', RecipesDetailView.as_view(), name='detail'),
   path('recipes/author/<int:pk>/', RecipesAuthorView.as_view(), name='author'),
   path("create/", create_recipe, name="create_recipe"),
   path("update/<int:pk>/", update_recipe, name="update_recipe"),
   path("delete/<int:pk>/", delete_recipe, name="delete_recipe"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)