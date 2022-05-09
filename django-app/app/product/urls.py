from django.urls import path

from .api import ProductApiView

urlpatterns = [
    path("products", ProductApiView.as_view({
        "get": "list",
        "post": "create"
    })),
    path("products/<str:pk>", ProductApiView.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    })),
]
