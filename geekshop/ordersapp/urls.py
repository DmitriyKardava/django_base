import ordersapp.views as ordersapp
from django.urls import path

app_name = 'orders_app'

urlpatterns = [
    path("", ordersapp.OrderList.as_view(), name="list"),
    path("create", ordersapp.create_order, name="create"),
    path("<int:pk>/", ordersapp.OrderUpdateView.as_view(), name="update"),
    path("pay/<int:pk>/", ordersapp.order_pay, name="pay"),
    path("cancel/<int:pk>/", ordersapp.order_cancel, name="cancel"),
]
