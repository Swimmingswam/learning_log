from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth import logout
# Create your views here.
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))