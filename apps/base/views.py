from django.contrib.auth import logout

# Create your views here.
from django.http import HttpResponseRedirect

# Create your views here.


def logout_view(request):
    # print("paso")
    logout(request)
    return HttpResponseRedirect("/admin/")


def admin_view(request):
    return HttpResponseRedirect("/admin/")
