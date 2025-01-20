# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='dashboard-home'),
# ]


from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.index, name='dashboard-home'),  # Correctly reference the index view
]
