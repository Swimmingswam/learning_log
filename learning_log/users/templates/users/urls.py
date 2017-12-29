from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
	url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
	url(r'^logout/$',views.logout_view,name="logout"),
	
]
app_name = 'users'   #django2新修改