from django.urls import path
from app import views
from app.views import lending, Creat_team


urlpatterns = [
   path('create/', views.create_event, name='create_event'),
   path('regi/', views.do_register, name='do_register'),
   path('list/', views.Event_list, name='Event_list'),
   path('events/<int:event_id>/', views.event_detail, name='event_detail'),
   path('person/', views.person_dtl, name='person'),
   path('lending/', lending.as_view(), name='lending'),
   path('Creat_team/', Creat_team.as_view(), name='Creat_team')
]
