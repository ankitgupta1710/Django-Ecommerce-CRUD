from django.urls import path, include
from product_app import views
from product_app.views import ProductList, ProductCreate, ProductUpdate, ProductDelete, ProductDetail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'product_app'

urlpatterns = [    
    path('', ProductList.as_view(), name = 'product_list'),
    path('product_create', ProductCreate.as_view(), name = 'product_create'),
    path('product_update/<pk>', ProductUpdate.as_view(), name = 'product_update'),
    path('product_delete/<pk>', ProductDelete.as_view(), name = 'product_delete'),
    path('product_detail/<pk>', ProductDetail.as_view(), name = 'product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


