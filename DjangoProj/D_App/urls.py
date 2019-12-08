from django.conf.urls import url
from D_App import views

urlpatterns = [
		
		url(r'^$',views.main,name = 'main')

]