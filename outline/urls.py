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
    path('update_completed/<int:id>', views.update_completed, name='update_completed'),
    path('delete_table/<int:id>', views.delete_table, name='delete_table'),
    path('app_password/', views.app_password, name='app_password'),
    path('add_app_password/', views.add_app_password, name='add_app_password'),
    path('all_events/<int:id>', views.all_events, name='all_events'),
    path('demo/', views.demo, name='demo'),
]