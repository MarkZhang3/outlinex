from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_event/', views.add_event, name="add_event"),
    path('add_table/', views.add_table, name="add_table"),
    path('add_event/add_event_to_record/', views.add_event_to_record, name="add_event_to_record"),
    path('add_table/add_table_to_record/', views.add_table_to_record, name="add_table_to_record"),
    path('delete_event/<int:id>', views.delete_event, name="delete_event"),
    path('update_event/<int:id>', views.update_event, name='update_event'),
    path('details/<int:id>', views.details, name='event_details'),
    path('/outline/update_completed/<int:id>', views.update_completed, name='update_completed'),
]