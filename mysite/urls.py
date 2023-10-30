from django.contrib import admin
from django.urls import path, include
# from apps.views import def_view
from django.http import HttpResponse


# #direct, simple way
def home(request):
    return HttpResponse('Hello Word!')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mytest/', include('mytest.urls'), name ='mytest'),
    # path('apps/', def_view, name='given_name'),
    path('',home),
]