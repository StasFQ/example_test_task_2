from django.urls import path

from generate.views import create_data_schema, generate_data, home

urlpatterns = [
    path('home/', home, name='home'),
    path('', create_data_schema, name='create_data_schema'),
    path('generate_data/<int:schema_id>/', generate_data, name='generate_data'),
]

