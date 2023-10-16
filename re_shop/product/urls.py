from django.urls import path, include
from . import views

app_name = "product"
urlpatterns = [
    path('',views.product),
    path('contacts/',views.contact),
    path('<int:my_id>/', views.ful_product, name = "detail")

]