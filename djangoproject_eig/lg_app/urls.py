from django.conf.urls import url
from lg_app import views


app_name = 'lg_app'

urlpatterns = [

    url(r'^register/$',views.register,name ='register'),
    url(r'^dj/$',views.django,name = 'django'),
    url(r'^user_login/$',views.user_login,name = 'user_login')



]