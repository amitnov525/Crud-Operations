from django.urls import path
from main import views
urlpatterns=[
    path('',views.Show_Add.as_view(),name='add'),
    path('delete/<int:pk>/',views.DeleteUser.as_view(),name='delete'),
    path('update/<int:pk>/',views.UpdateUser.as_view(),name="update"),
]