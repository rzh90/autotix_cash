from django.urls import path

from . import views

app_name = 'cash'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('shows/', views.shows, name='shows'),
    path('shows/<int:show_id>/', views.show, name='show'),
    path('new_show/', views.new_show, name='new_show'),
    path('new_spent/<int:show_id>/', views.new_spent, name='new_spent'),
    path('edit_spent/<int:spent_id>/', views.edit_spent, name='edit_spent'),
    path('delete_spent/<int:spent_id>/', views.delete_spent, name='delete_spent'),
]
