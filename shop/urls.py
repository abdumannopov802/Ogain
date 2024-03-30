from django.urls import path
from . import views

urlpatterns = [
    path('blog-details', views.blog_details, name='blog-details'),
    path('blog', views.blog, name='blog'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('', views.index, name='home'),
    path('main', views.main, name='main'),
    path('shop-details', views.shop_details, name='shop-details'),
    path('shop-grid', views.shop_grid, name='shop-grid'),
    path('shopping-cart', views.shopping_cart, name='shopping-cart'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
