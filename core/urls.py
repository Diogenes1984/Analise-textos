from django.urls import path
from .views import IndexView, texto


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('texto/', texto, name='texto'),
    # path('resultado/', semelhanca, name='semelhanca'),

]
