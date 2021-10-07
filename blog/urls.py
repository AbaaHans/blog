from django.urls import path

#appel aux vues
from . import views


urlpatterns = [
    
    path('',views.home, name="home" ),
    path('artiicle/<int:id_article>',views.detail, name="detail")
   
]
