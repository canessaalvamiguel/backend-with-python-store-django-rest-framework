from django.urls import path

from .views import ShoppingCartAPIView

urlpatterns = [
    path('cart-items/', ShoppingCartAPIView.as_view()),
    path('cart-items/<int:id>', ShoppingCartAPIView.as_view())
]