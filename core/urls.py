from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RestaurantViewSet, MenuItemViewSet, CartViewSet,
    OrderViewSet, ReviewViewSet, CouponViewSet,
    register_user, login_user,
    register_page, login_page,
    restaurant_list_page, restaurant_detail,
    add_to_cart, view_cart, update_cart, remove_from_cart, place_order, my_orders,
)

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'cart', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'coupons', CouponViewSet)

urlpatterns = [
    path('', restaurant_list_page, name='restaurant_list'),

    # 👉 Page URLs (HTML render)
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('restaurant/<int:pk>/', restaurant_detail, name='restaurant_detail'),
    path('add-to-cart/<int:menu_item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/update/<int:cart_id>/', update_cart, name='update_cart'),
    path('cart/remove/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/place-order/', place_order, name='place_order'),
    path('my-orders/', my_orders, name='my_orders'),

    # 👉 API URLs (JSON response)
    path('api/register/', register_user, name='register_user'),
    path('api/login/', login_user, name='login_user'),
    path('api/', include(router.urls)),
]

