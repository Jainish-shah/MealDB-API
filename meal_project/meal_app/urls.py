from django.urls import URLPattern, path
from product_app import views

urlpatterns = [
    path('', views.get_meals, name = "get_meals"),
    path('meals/<int:id>/', views.meal_detail, name = "meal_detail")
]