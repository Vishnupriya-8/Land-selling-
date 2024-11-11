from django.urls import path
from django.conf import settings
from .import views
from django.conf.urls.static import static

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/',views.log_in, name='login'),
    path('view/',views.view,name='view'),
    path('add/', views.add_plot, name='add'),
    path('logout/',views.log_out, name='logout'),
    path('delete/<int:land_id>/', views.delete_land, name='delete'),
    path('edit/<int:land_id>/',views.edit_land,name='edit'),
    path('my_plots/', views.my_plots, name='my_plots')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
