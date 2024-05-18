from django.urls import path
from app.views import tabsetor_list, servativ_list, tabsetor_detail_change_and_delete, servativ_detail_change_and_delete

urlpatterns = [
    path('tabsetor/', tabsetor_list),
    # path(r'^/(?P<codigo>[0-9])/$', tabsetor_detail_change_and_delete)
    # path('<pk>/', tabsetor_detail_change_and_delete)
    path("tabsetor/<str:codigo>/", tabsetor_detail_change_and_delete),
    path('servativ/', servativ_list),
    path("servativ/<str:mat_siape>/", servativ_detail_change_and_delete)
]