from django.urls import path
from .views import GameView

app_name = 'game'

urlpatterns = [
    path('', GameView.as_view(), name='game')
]
